
import ipaddress

print("===== IP ADDRESS VALIDATOR =====")

ip_input = input("Enter an IPv4 address: ")

try:
    ip = ipaddress.ip_address(ip_input)

    print("\n===== IP INFORMATION =====")
    print("IP Address:", ip)
    print("Version:", ip.version)

    if ip.is_private:
        print("Address Type: Private IP")
    elif ip.is_global:
        print("Address Type: Public IP")
    else:
        print("Address Type: Special-purpose IP")

    print("Valid IP Address: Yes")

except ValueError:
    print("\nInvalid IP address!")
    print("Please enter a valid IPv4 or IPv6 address.")
