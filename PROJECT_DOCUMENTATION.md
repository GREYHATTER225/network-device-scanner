<h1 align="center"> Network Device Scanner – Documentation </h1>


## 📌 Problem
Users cannot easily see what devices are connected to their network. Unknown devices may go unnoticed.

## 🎯 Objective
To build a tool that scans the network and identifies connected devices, highlighting unknown ones.

## 🧠 Solution
The system performs network scanning using ARP requests and collects responses from active devices. It compares results with previously saved devices.

## ⚙️ Working

1. Send ARP request to all IPs in network range  
2. Devices respond with MAC address  
3. Vendor is identified using API  
4. Devices compared with known list  
5. Unknown devices are flagged  
## 🔍 Features

- Network scanning  
- Vendor identification  
- Known vs unknown detection  
- Risk classification  
- Logging system  

## 📊 Output

- List of devices  
- Risk level (LOW / HIGH)  
- Reason for classification  

## 🚀 Conclusion

This tool provides basic visibility into a network and helps detect unknown devices using simple logic.