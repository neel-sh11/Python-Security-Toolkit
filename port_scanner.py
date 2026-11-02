




import socket

print("===== TCP PORT SCANNER =====")

target = "127.0.0.1"

services = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP Alternative"
}

open_ports = []

print("Target:", target)
print("Scanning ports...\n")

for port, service in services.items():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)

    try:
        result = client.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} ({service}) - OPEN")
            open_ports.append(port)
        else:
            print(f"Port {port} ({service}) - CLOSED or FILTERED")

    except socket.error as error:
        print(f"Port {port} - ERROR: {error}")

    finally:
        client.close()

print("\n===== SCAN SUMMARY =====")
print("Total ports scanned:", len(services))
print("Open ports:", len(open_ports))

if open_ports:
    print("Open port numbers:", open_ports)
else:
    print("No open ports detected.")

print("Scan completed.")
