Python Security Toolkit 🔐

A beginner-friendly Python project focused on learning basic cybersecurity concepts through practical tools.

📌 Project Overview

This repository contains small Python-based security tools developed as part of my cybersecurity learning journey.

The first tool is a Password Strength Checker that analyzes basic password characteristics and provides a simple security rating.

🛠️ Current Tools

1. Password Strength Checker

The program checks whether a password contains:

* At least 8 characters
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Based on these checks, it generates a security score out of 5 and classifies the password as:

* Weak
* Moderate
* Strong

💻 Technologies Used

* Python
* Python string module

🚀 How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

python password_checker.py

4. Enter a test password when prompted.

🧪 Example

Input:

Hello@123

Example Output: Strong

 2. Secure Password Generator

Generates random passwords using Python's `secrets` module.

Features:

- Custom password length
- Minimum length validation
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Cryptographically stronger random generation using `secrets`

 3. SHA-256 Hash Generator

A Python-based utility that generates SHA-256 cryptographic hashes from text input.

Features:
- Generates SHA-256 hashes
- Uses Python hashlib library
- Converts text into bytes
- Produces 64-character hexadecimal digests
- Handles empty input

Concepts Practiced:
- Cryptographic hashing
- SHA-256
- Hash functions
- Data integrity
- Python hashlib


4. Login Attempt Analyzer

A Python-based security utility that analyzes login activity and identifies suspicious failed login attempts.

Features:
- Tracks failed login attempts
- Groups attempts by IP address
- Detects repeated failed attempts
- Flags suspicious login activity
- Generates a basic security report

Concepts Practiced:
- Security log analysis
- Python dictionaries
- Data processing
- Conditional statements
- Basic SOC monitoring concepts

 Improve TCP port scanner with service 
 
 5. File Integrity Monitor

A Python-based security utility that detects file modifications using SHA-256 cryptographic hashing.

Features:
- Calculates SHA-256 file hashes
- Reads files in binary mode
- Stores an original hash for comparison
- Detects file modifications
- Generates a security alert when changes are detected

Concepts Practiced:
- File integrity monitoring (FIM)
- Cryptographic hashing
- SHA-256
- Python file handling
- Data integrity and tampering detection

  
 7. Log File Analyzer

A Python-based security utility that reads login records from a text file and detects repeated failed login attempts.

Features:
- Reads login records from a text file
- Counts successful and failed logins
- Tracks failed attempts by IP address
- Identifies suspicious IP addresses
- Detects invalid log records
- Generates a security summary

Concepts Practiced:
- File handling
- Log analysis
- Python dictionaries
- Data processing
- Basic SOC monitoring


 8. IP Address Validator

A Python utility that validates IP addresses and identifies their address categories.

Features:
- Validates IPv4 and IPv6 addresses
- Identifies private and public IP addresses
- Detects invalid IP formats
- Displays IP version information
- Handles invalid input safely

Concepts Practiced:
- IP addressing
- IPv4 and IPv6
- Private and public IP ranges
- Python ipaddress module
- Exception handling
  



===== PASSWORD SECURITY REPORT =====
Password Length: 9
Security Score: 5 / 5
Password Strength: Strong
====================================

📚 Concepts Practiced

* Python functions
* Conditional statements
* Loops
* String handling
* Input validation
* The any() function
* Basic password security concepts

⚠️ Limitations

This is a beginner-level educational project.

The tool evaluates basic character composition only. It does not check:

* Whether a password has been leaked
* Whether a password is commonly used
* Password entropy
* Dictionary-based attacks

A high score does not guarantee that a password is secure.

🔮 Future Improvements

* Add password entropy estimation
* Detect common passwords
* Improve password recommendations
* Create additional security tools

⸻

👨‍💻 Author

Neel

BCA Student | Aspiring Cybersecurity Professional

GitHub Profile
