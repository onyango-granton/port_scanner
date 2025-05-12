# PORT SCANNER

A simple yet powerful Python-based port scanner that checks for open ports on a target host. It features:

- Clean ASCII banner via `pyfiglet`
- Progress bar using `tqdm`
- Full port range scan (1-65534)
- Error handling for hostname resolution and connectivity issues

---

## Project Structure

```
port-scanner/
├── main.py
└── README.md
```

---

## Features

- Scans all TCP ports (1-65534) on a target IP or domain
- ASCII art title banner
- Real-time progress bar display
- Graceful error handling (invalid hostnames, server issues, interruptions)
- Displays timestamps for when scanning starts

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```text
pyfiglet
tqdm
```

> **Note:** You must be running Python 3.6 or later.

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/onyango-granton/port-scanner.git
    cd port-scanner
    ```

2. Install required packages:

    ```bash
    pip install pyfiglet tqdm
    ```

---

## Usage

Run the script with a target IP address or hostname:

```bash
python main.py <target>
```

Example:

```bash
python main.py 8.8.8.8
```

### Output Example:

```
 ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  
|  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
| |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
|  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
|_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\


Scanning 127.0.0.1 started at: 2025-05-12 18:28:06.216854
Progress: 100%|████████████████████████████████████████| 65534/65534
Port 53 is open
```

---

## Notes

- Scanning all 65k+ ports can take time depending on the target's responsiveness.
- Some systems or networks may block port scans. Always scan with permission.
- You can reduce the port range or optimize with threading for faster results.

---

## Code Overview

- Uses `socket` to establish TCP connections.
- Uses `connect_ex()` which returns `0` if the port is open.
- Adds a timeout of 1 second per port to avoid hanging.
- Handles:
  - `KeyboardInterrupt` (Ctrl+C)
  - `socket.gaierror` (bad hostname)
  - `socket.error` (server not reachable)

---

## Disclaimer

This tool is for **educational and authorized security testing purposes only**. Unauthorized scanning is illegal and unethical.

---

## Author

**Granton Onyango**

> Built with love for Python, networking, and CLI tools.