# BT Tracker 检测工具

## 简介

本项目提供一个 Python 程序，用于检测 BitTorrent Tracker（包括 HTTP/HTTPS、UDP 以及 wss 协议）的连通性，并自动过滤掉失效的 Tracker 地址。程序将从输入文本文件中读取 Tracker 地址，依次检测其状态，过滤掉无效地址后将有效地址按字母顺序排序，输出到新的文本文件中。

## 功能

- **多协议支持：**  
  支持 HTTP/HTTPS、UDP 和 wss 协议的 Tracker 检测。

- **自动过滤：**  
  自动过滤掉无法正常响应的 Tracker 地址。

- **排序输出：**  
  将有效 Tracker 地址按字母顺序排序后写入输出文件，确保每行一个地址，便于管理和使用。

- **易于扩展：**  
  代码结构清晰，可根据需要扩展其他协议或检测方法。

## 依赖

在运行该程序之前，请确保已安装以下 Python 库：

- [requests](https://pypi.org/project/requests/)  
- [websockets](https://pypi.org/project/websockets/)

安装方式：

```bash
pip install requests websockets
```

## 使用方法

1. **准备 Tracker 列表：**  
   在项目目录下创建一个名为 `trackers.txt` 的文件，每行写入一个 Tracker 地址。

2. **运行程序：**  
   执行脚本：
   ```bash
   python tracker_checker.py
   ```
   程序会依次检测每个 Tracker 地址，并将有效地址输出到 `filtered_trackers.txt` 文件中。

3. **查看结果：**  
   检查 `filtered_trackers.txt` 文件，里面包含经过过滤和排序的有效 Tracker 地址。

## 代码结构

- **tracker_checker.py**  
  主程序文件，包含所有协议检测函数和文件处理逻辑：
  
  - **check_http_tracker(url, timeout):**  
    使用 `requests.head` 检查 HTTP/HTTPS Tracker 的连通性。
  
  - **check_udp_tracker(url, timeout):**  
    根据 UDP Tracker 协议发送连接请求，并解析响应数据。
  
  - **check_wss_tracker_async(url, timeout) / check_wss_tracker(url, timeout):**  
    使用 `websockets` 库检测 wss 协议 Tracker 的连通性。
  
  - **check_tracker(url):**  
    根据 URL 中的协议（scheme）自动调用相应检测函数。
  
  - **main():**  
    读取输入文件 `trackers.txt`，检测每个 Tracker 地址，过滤、排序后写入输出文件 `filtered_trackers.txt`。

## 许可协议

本项目采用 MIT 许可协议。详情请参阅 [LICENSE](LICENSE) 文件。

## 联系方式

如有问题或建议，请提交 issue 或直接联系项目维护者。

## 赞助

![pay](pay.jpg)
