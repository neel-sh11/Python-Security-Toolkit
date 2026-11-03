



# Login Attempt Analyzer


logs = [
    "FAILED alice 192.168.1.10",
    "FAILED bob 192.168.1.20",
    "SUCCESS alice 192.168.1.10",
    "FAILED admin 192.168.1.50",
    "FAILED admin 192.168.1.50",
    "FAILED admin 192.168.1.50",
    "FAILED john 192.168.1.20"
]

failed_attempts = {}

for log in logs:
    details = log.split()

    status = details[0]
    username = details[1]
    ip_address = details[2]

    if status == "FAILED":
        if ip_address in failed_attempts:
            failed_attempts[ip_address] += 1
        else:
            failed_attempts[ip_address] = 1

print("===== LOGIN SECURITY REPORT =====")

if not failed_attempts:
    print("No failed login attempts found.")

for ip, count in failed_attempts.items():
    print("IP Address:", ip)
    print("Failed Attempts:", count)

    if count >= 3:
        print("ALERT: Suspicious login activity!")
    else:
        print("Status: Normal")

    print("-----------------------------")

print("Analysis completed.")
