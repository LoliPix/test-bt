import asyncio
import socket
import struct
import random
import requests
import websockets
from urllib.parse import urlparse

# 检测 HTTP/HTTPS Tracker
def check_http_tracker(url, timeout=5):
    try:
        # 使用 HEAD 请求检测（部分 Tracker 可能只支持 GET）
        response = requests.head(url, timeout=timeout)
        if response.status_code in [200, 302, 403]:
            return True
        else:
            return False
    except Exception:
        return False

# 检测 UDP Tracker
def check_udp_tracker(url, timeout=5):
    parsed = urlparse(url)
    host = parsed.hostname
    port = parsed.port
    if not host or not port:
        return False

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    try:
        # 协议规定的初始 connection_id（8 字节）
        connection_id = 0x41727101980
        action = 0  # 连接请求
        transaction_id = random.randint(0, 0xFFFFFFFF)
        req = struct.pack(">qii", connection_id, action, transaction_id)
        sock.sendto(req, (host, port))
        data, _ = sock.recvfrom(16)
        if len(data) < 16:
            return False
        res_action, res_transaction_id, _ = struct.unpack(">iiq", data)
        # 检查响应是否正确：action 应为 0 且 transaction_id 与请求一致
        if res_action == 0 and res_transaction_id == transaction_id:
            return True
        else:
            return False
    except Exception:
        return False
    finally:
        sock.close()

# 异步检测 wss:// Tracker
async def check_wss_tracker_async(url, timeout=5):
    try:
        async with websockets.connect(url, timeout=timeout) as ws:
            # 如果连接成功，认为 Tracker 有效
            return True
    except Exception:
        return False

# 同步封装异步检测 wss:// Tracker 的方法
def check_wss_tracker(url, timeout=5):
    return asyncio.run(check_wss_tracker_async(url, timeout))


# 综合检测函数，根据 URL 协议选择检测方式
def check_tracker(url):
    parsed = urlparse(url)
    scheme = parsed.scheme
    if scheme in ["http", "https"]:
        return check_http_tracker(url)
    elif scheme == "udp":
        return check_udp_tracker(url)
    elif scheme == "wss":
        return check_wss_tracker(url)
    else:
        # 对于未知协议，一律认为无效
        return False

def main():
    input_file = "trackers.txt"          # 输入文件，存放所有待检测 Tracker 地址（每行一个地址）
    output_file = "filtered_trackers.txt"  # 输出文件，保存过滤后的有效 Tracker 地址

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            trackers = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"读取输入文件出错: {e}")
        return

    valid_trackers = []
    print("开始检测 Tracker 服务器状态...")
    for tracker in trackers:
        print(f"检测: {tracker}")
        if check_tracker(tracker):
            print(f"有效: {tracker}")
            valid_trackers.append(tracker)
        else:
            print(f"无效: {tracker}")

    # 排序（按字母顺序）
    valid_trackers.sort()

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for tracker in valid_trackers:
                f.write(tracker + "\n")
        print(f"\n检测完成，共 {len(valid_trackers)} 个有效 Tracker，已保存至 {output_file}")
    except Exception as e:
        print(f"写入输出文件出错: {e}")

if __name__ == "__main__":
    main()
