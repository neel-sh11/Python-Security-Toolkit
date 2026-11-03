


from datetime import datetime

print("===== SECURITY AUDIT REPORT GENERATOR =====")

# Sample security audit settings
security_checks = {
    "Strong password policy": True,
    "Multi-factor authentication": False,
    "Firewall enabled": True,
    "Regular software updates": False,
    "Antivirus protection": True,
    "Data backup enabled": True,
    "Unused accounts disabled": False
}

total_checks = len(security_checks)
passed_checks = 0
failed_checks = []

print("\n===== SECURITY CHECK RESULTS =====")

for check, status in security_checks.items():

    if status:
        print("[PASS]", check)
        passed_checks += 1

    else:
        print("[FAIL]", check)
        failed_checks.append(check)

# Calculate security score
score = (passed_checks / total_checks) * 100

print("\n===== SECURITY SUMMARY =====")

print("Total Checks:", total_checks)
print("Passed Checks:", passed_checks)
print("Failed Checks:", len(failed_checks))
print("Security Score:", round(score, 2), "%")

# Determine security rating
if score >= 85:
    rating = "Good"
elif score >= 60:
    rating = "Moderate"
else:
    rating = "Poor"

print("Security Rating:", rating)

# Generate report
report = []
report.append("===== SECURITY AUDIT REPORT =====")
report.append("Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
report.append("Security Score: " + str(round(score, 2)) + "%")
report.append("Security Rating: " + rating)
report.append("\nFailed Security Checks:")

if failed_checks:
    for item in failed_checks:
        report.append("- " + item)
else:
    report.append("No failed checks.")

report.append("\nRecommendations:")

for item in failed_checks:
    report.append("- Review and improve: " + item)

report.append("\nAudit completed.")

# Save report to a text file
with open("security_audit_report.txt", "w") as file:
    file.write("\n".join(report))

print("\nAudit report generated successfully!")
print("File: security_audit_report.txt")

