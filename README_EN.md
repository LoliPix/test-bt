# BT Tracker Checker

## Introduction

This project provides a Python script that checks the connectivity of BitTorrent Trackers, including HTTP/HTTPS, UDP, and wss protocols. The script reads Tracker addresses from an input text file, verifies their status, filters out the inactive ones, and outputs the valid Tracker addresses in alphabetical order to an output file.

## Features

- **Multi-Protocol Support:**  
  Supports checking Tracker connectivity for HTTP/HTTPS, UDP, and wss protocols.

- **Automatic Filtering:**  
  Automatically filters out inactive Tracker addresses.

- **Sorted Output:**  
  Outputs the valid Tracker addresses sorted in alphabetical order (one address per line) for easy management and use.

- **Extensible:**  
  The code is structured clearly and can be easily extended to support additional protocols or checking methods.

## Dependencies

Before running the script, make sure you have installed the following Python libraries:

- [requests](https://pypi.org/project/requests/)
- [websockets](https://pypi.org/project/websockets/)

Installation:

```bash
pip install requests websockets
```

## Usage

1. **Prepare Tracker List:**  
   Create a file named `trackers.txt` in the project directory, with one Tracker address per line.

2. **Run the Script:**  
   Execute the script:
   ```bash
   python tracker_checker.py
   ```
   The script will check each Tracker address and output the valid ones into the `filtered_trackers.txt` file.

3. **Review the Output:**  
   Check the `filtered_trackers.txt` file, which contains the valid Tracker addresses sorted alphabetically.

## Code Structure

- **tracker_checker.py**  
  The main script file that includes all protocol checking functions and file handling logic:
  
  - **check_http_tracker(url, timeout):**  
    Uses `requests.head` to check the connectivity of HTTP/HTTPS Trackers.
  
  - **check_udp_tracker(url, timeout):**  
    Sends a connection request according to the UDP Tracker protocol and parses the response.
  
  - **check_wss_tracker_async(url, timeout) / check_wss_tracker(url, timeout):**  
    Uses the `websockets` library to check the connectivity of wss protocol Trackers.
  
  - **check_tracker(url):**  
    Automatically calls the appropriate checking function based on the URL scheme.
  
  - **main():**  
    Reads the input file `trackers.txt`, checks each Tracker address, filters, sorts, and writes the valid addresses to the output file `filtered_trackers.txt`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, please submit an issue or contact the project maintainer directly.

## sponsor

![pay](pay.jpg)
