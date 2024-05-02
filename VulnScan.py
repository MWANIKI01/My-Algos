import subprocess

def print_scan_types():
    print("-sS: TCP SYN scan (stealth scan)")
    print("-sT: TCP connect scan")
    print("-sU: UDP scan")
    print("-sN: TCP null scan (no flags set)")
    print("-sF: TCP FIN scan (FIN flag set)")
    print("-sX: TCP Xmas scan (FIN, SYN, and URG flags set)")
    print("-sA: OS detection, version detection, script scanning, and traceroute")
    print("-sV: Version detection")
    print("-p-: Scan all ports")

def scan_vulnerabilities(ip_address, scan_type):
    command = f"nmap {scan_type} {ip_address}"
    print(f"Running command: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error: {result.stderr}")
    except Exception as e:
        print(f"Error: {e}")

ip_address = input("Enter the IP address to scan: ")
while True:
   
    scan_type = input("Enter the scan type or 'options' to see available scan types: ")
    if scan_type.lower() == "options":
     print_scan_types()
       
    else:
        scan_vulnerabilities(ip_address, scan_type)
        break

output = scan_vulnerabilities(ip_address, scan_type)
print(output)
