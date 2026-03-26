<h1 align="center">Network Device Scanner</h1>

<p align="center">
Scan your network • Detect unknown devices • Understand what’s connected
</p>

## ⚡ What this tool does

- Finds devices connected to your WiFi  
- Shows IP + MAC + Vendor  
- Detects unknown devices  
- Marks risk based on previous scans  

## 🧠 How it thinks

First run → learns your network  
Next runs → compares and flags anything new  


## 🔍 Example Output
IP              MAC Address         Vendor         Risk  Reason
----------------------------------------------------------------
192.168.x.x     xx:xx:xx            Samsung        LOW   Known device
192.168.x.x     xx:xx:xx            Unknown        HIGH  New device

## 🛠️ Run it
pip install scapy requests
python scanner.py


---

## 📁 Files

- `scanner.py` → main logic  
- `known_devices.json` → remembers devices  
- `scan_log.txt` → scan history  


## 📌 Idea behind it

Instead of just scanning, this tool:
- remembers devices  
- detects changes  
- highlights unknown activity  


## ⚠️ Note

Works on local network only.  
Used for learning and basic monitoring.

# network-device-scanner
