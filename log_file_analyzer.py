
# Project 7: Log File Analyzer
# Python Security Toolkit

import os

filename = "login_logs.txt"

# Create sample log file if it does not exist
if not os.path.exists(filename):
    sample_logs = [
        "FAILED alice 192.168.1.10",
        "SUCCESS alice 192.168.1.10",
        "FAILED bob 192.168.1.20",
        "FAILED admin 192.168.1.50",
        "FAILED admin 192.168.1.50",
        "FAILED admin 192.168.1.50",
        "SUCCESS john 192.168.1.20",
        "FAILED john 192.168.1.20"
    ]

    with open(filename, "w") as file:
        for log in sample_logs:
            file.write(log + "\n")

# Initialize counters
successful_logins = 0
failed_logins = 0
failed_attempts = {}
invalid_records = 0

# Read and analyze the log file
with open(filename, "r") as file:
    for line in file:
        details = line.strip().split()

        if len(details) != 3:
            invalid_records += 1
            continue

        status, username, ip_address = details

        if status == "FAILED":
            failed_logins += 1

            if ip_address in failed_attempts:
                failed_attempts[ip_address] += 1
            else:
                failed_attempts[ip_address] = 1

        elif status == "SUCCESS":
            successful_logins += 1

        else:
            invalid_records += 1

# Generate security report
print("===== LOG FILE SECURITY ANALYZER =====")

print("\nLog File:", filename)
print("Successful Logins:", successful_logins)
print("Failed Logins:", failed_logins)
print("Invalid Records:", invalid_records)

print("\n===== SUSPICIOUS IP ANALYSIS =====")

suspicious_count = 0

for ip, count in failed_attempts.items():
    print("IP Address:", ip)
    print("Failed Attempts:", count)

    if count >= 3:
        print("ALERT: Suspicious Activity Detected!")
        suspicious_count += 1
    else:
        print("Status: Normal")

    print("-----------------------------")

print("\n===== FINAL SECURITY SUMMARY =====")
print("Total Failed Logins:", failed_logins)
print("Suspicious IP Addresses:", suspicious_count)
print("Analysis Completed.")
