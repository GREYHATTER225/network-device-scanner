from scapy.all import ARP, Ether, srp
import requests
import json
from datetime import datetime

KNOWN_FILE = "known_devices.json"
LOG_FILE = "scan_log.txt"

# ----------------------------
# Vendor lookup
# ----------------------------
def get_vendor(mac):
    try:
        res = requests.get(f"https://api.macvendors.com/{mac}", timeout=3)
        return res.text if res.status_code == 200 else "Unknown"
    except:
        return "Unknown"

# ----------------------------
# Load known devices
# ----------------------------
def load_known():
    try:
        with open(KNOWN_FILE, "r") as f:
            return json.load(f)
    except:
        return []

# ----------------------------
# Save known devices
# ----------------------------
def save_known(devices):
    with open(KNOWN_FILE, "w") as f:
        json.dump(devices, f, indent=4)

# ----------------------------
# Log scan
# ----------------------------
def log(devices):
    with open(LOG_FILE, "a") as f:
        f.write(f"\n[{datetime.now()}]\n")
        for d in devices:
            f.write(f"{d['ip']} | {d['mac']} | {d['vendor']}\n")

# ----------------------------
# Scan network
# ----------------------------
def scan(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []
    for _, r in result:
        mac = r.hwsrc
        devices.append({
            "ip": r.psrc,
            "mac": mac,
            "vendor": get_vendor(mac)
        })
    return devices

# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    ip_range = "192.168.176.0/24"

    print("\nScanning network...\n")

    devices = scan(ip_range)
    known = load_known()
    known_macs = [d["mac"] for d in known]
    has_known = len(known) > 0

    new_devices = []

    if has_known:
        print("{:<15} {:<20} {:<20} {:<6} {}".format("IP", "MAC", "Vendor", "Risk", "Reason"))
        print("-" * 90)
        for d in devices:
            if d["mac"] in known_macs:
                risk = "LOW"
                reason = "Known device (seen before)"
            else:
                risk = "HIGH"
                reason = "New/Unknown device"
                new_devices.append(d)

            print("{:<15} {:<20} {:<20} {:<6} {}".format(
                d["ip"], d["mac"], d["vendor"], risk, reason
            ))
    else:
        print("{:<15} {:<20} {:<20}".format("IP", "MAC", "Vendor"))
        print("-" * 60)
        for d in devices:
            print("{:<15} {:<20} {:<20}".format(
                d["ip"], d["mac"], d["vendor"]
            ))

    # Alert
    if new_devices:
        print("\n⚠️ ALERT: Unknown devices detected")
        for d in new_devices:
            print(f"{d['ip']} ({d['vendor']})")

    # Save known devices first time
    if not known:
        save_known(devices)
        print("\nSaved current devices as trusted")

    # Log scan
    log(devices)
    