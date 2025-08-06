# 🔍 Python Port Scanner

A fast and multithreaded TCP port scanner built with Python. It scans a user-specified range of ports on a remote host, shows real-time status (open/closed), and saves the results to a `.txt` file.

## 🚀 Features

- ✅ Multithreaded scanning using `ThreadPoolExecutor`
- 🎯 Scans custom port ranges on any target host
- ⏱️ User-defined timeout for socket connections
- 🌈 Color-coded terminal output using `colorama`
- 📁 Exports all scan results to a `.txt` file
- 📦 Cross-platform support (Linux, macOS, Windows)

## 🛠️ Requirements

- Python 3.6+
- `colorama`  
  Install with:

  ```bash
  pip install colorama
  ```

## 📄 Usage

1. Clone or download the script:

   ```bash
   git clone https://github.com/AkinwandeFredrick/Port-scanner
   cd port-scanner
   ```

2. Run the scanner:

   ```bash
   python port_scanner.py
   ```

3. Provide input when prompted:
   - Remote host (e.g. `scanme.nmap.org`)
   - Port range (start and end ports)
   - Timeout value (e.g. `0.5`)

4. Results will display on-screen and be saved to:
   ```
   scan_results_<host>.txt
   ```

## 📷 Sample Output

```
Enter a remote host to scan: scanme.nmap.org
Enter the start port: 20
Enter the end port: 100
Enter timeout in seconds: 1

Port 22: Open
Port 23: Closed
...
Scan completed in: 0:00:10.123456
Results saved to: scan_results_scanme_nmap_org.txt
```

## ⚠️ Disclaimer

This tool is for educational and authorized testing **only**. Do not scan systems you do not own or have explicit permission to test.

## 📚 License

MIT License

---

> Created by [AKINWANDE-Fredrick] 
