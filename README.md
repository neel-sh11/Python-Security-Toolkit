Python Security Toolkit

A collection of beginner-friendly Python projects focused on cybersecurity fundamentals, security automation, and practical programming.

This repository includes 12 small projects covering password security, file integrity, network scanning, log analysis, and other security-related concepts.

Projects

01. Password Checker

* Evaluates password strength using basic security rules.
* Checks length, uppercase, lowercase, digits, and special characters.

02. Secure Password Generator

* Generates random passwords using Python’s secrets module.
* Includes uppercase, lowercase, numbers, and special characters.

03. SHA-256 Text Hash Generator

* Generates SHA-256 hashes from user-provided text.
* Uses Python’s built-in hashlib module.
* Converts text into UTF-8 before hashing.
* Handles empty input.
* Demonstrates basic cryptographic hashing and data integrity concepts.

04. Login Attempt Analyzer

* Analyses sample login records.
* Identifies repeated failed login attempts and suspicious IP addresses.

05. TCP Port Scanner

* Checks selected TCP ports on a target system.
* Demonstrates basic network scanning using Python sockets.

06. File Integrity Monitor

* Calculates SHA-256 hashes of files using Python’s hashlib module.
* Reads file data in chunks for hashing.
* Compares original and updated hash values.
* Detects simulated file modifications.
* Demonstrates basic file integrity monitoring.

07. Log File Analyzer

* Reads and analyses login log records.
* Counts successful and failed logins and flags suspicious activity.

08. IP Address Validator

* Validates IPv4 and IPv6 addresses.
* Identifies address types using Python’s ipaddress module.
* * Classifies addresses as private, public, or special-purpose.
* Handles invalid input using exception handling.

09. Suspicious URL Checker

* Checks URLs for potentially suspicious characteristics.
* Uses basic rules to identify possible risks.

10. File Metadata Inspector

* Extracts file name, extension, size, and timestamps.
* Generates a SHA-256 hash for the inspected file.

11. Caesar Cipher Tool

* Encrypts and decrypts text using a shift-based substitution technique.
* Supports uppercase and lowercase letters.
* Preserves spaces, numbers, and special characters.
* Validates shift values and handles invalid input.

12. Security Audit Report Generator

* Evaluates simulated security controls.
* Generates a basic security audit report.

Technologies Used

* Python 3
* hashlib
* secrets
* socket
* ipaddress
* urllib
* os
* datetime
* mimetypes

Learning Objectives

* Understand cybersecurity fundamentals.
* Explore password security and cryptographic hashing.
* Practise basic network and log analysis.
* Learn file integrity monitoring.
* Develop Python scripting and problem-solving skills.

Disclaimer

These projects are developed for educational purposes. Some tools use simulated data and simplified security checks. They are not substitutes for professional security tools or production-grade assessments.

About

Created as part of my learning journey in Python and cybersecurity.

Focus Areas: Cybersecurity | Security Monitoring | Python Automation | Information Security

Author: Neel

