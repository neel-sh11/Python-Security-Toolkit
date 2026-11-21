

from urllib.parse import urlparse
import ipaddress

print("===== SUSPICIOUS URL CHECKER =====")

url = input("Enter a URL to check: ").strip()

suspicious_words = [
    "login", "verify", "account",
    "update", "secure", "banking",
    "password", "confirm"
]

risk_score = 0
warnings = []

# Add scheme if missing
if "://" not in url:
    url = "https://" + url

parsed_url = urlparse(url)
hostname = parsed_url.hostname

if not hostname:
    print("\nInvalid URL: No valid hostname found.")
else:
    # Check HTTPS
    if parsed_url.scheme.lower() != "https":
        risk_score += 2
        warnings.append("URL does not use HTTPS.")

    # Check suspicious keywords
    for word in suspicious_words:
        if word in url.lower():
            risk_score += 1
            warnings.append(
                "Suspicious keyword detected: " + word
            )

    # Check whether hostname is an IP address
    try:
        ipaddress.ip_address(hostname)
        risk_score += 2
        warnings.append("URL uses an IP address as hostname.")
    except ValueError:
        pass

    # Check URL length
    if len(url) > 100:
        risk_score += 1
        warnings.append("Unusually long URL.")

    # Check unusual symbols in hostname
    if "@" in parsed_url.netloc:
        risk_score += 2
        warnings.append("URL contains an @ symbol in its authority.")

    # Security report
    print("\n===== URL SECURITY REPORT =====")
    print("URL:", url)
    print("Hostname:", hostname)
    print("Risk Score:", risk_score)

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print("-", warning)
    else:
        print("\nNo suspicious patterns detected.")

    print("\n===== FINAL ASSESSMENT =====")

    if risk_score >= 4:
        print("HIGH RISK: Suspicious URL patterns detected.")
    elif risk_score >= 2:
        print("MEDIUM RISK: Review this URL carefully.")
    else:
        print("LOW RISK: Few suspicious patterns detected.")

    print("\nAnalysis completed.")
