Python Security Toolkit

A collection of beginner-friendly Python projects focused on cybersecurity fundamentals, security automation, and practical programming.

This repository includes 12 small projects covering password security, file integrity, network scanning, log analysis, and other security-related concepts.

Projects

01. Password Strength Checker

* Evaluates password strength using five basic security criteria.
* Checks length, uppercase, lowercase, digits, and special characters.
* Calculates a security score out of five.
* Classifies passwords as weak, moderate, or strong.
* Provides basic password improvement suggestions.
  
02. Secure Password Generator

* Generates random passwords using Python’s secrets module.
* Supports uppercase, lowercase, digits, and special characters.
* Ensures character variety in every generated password.
* Uses secure random selection and shuffling.
* Validates password length before generation.

03. SHA-256 Text Hash Generator

* Generates SHA-256 hashes from user-provided text.
* Uses Python’s built-in hashlib module.
* Converts text into UTF-8 before hashing.
* Handles empty input.
* Demonstrates basic cryptographic hashing and data integrity concepts.

04. Login Attempt Analyzer

* Analyses predefined login records using Python.
* Tracks failed login attempts by IP address.
* Identifies repeated failed authentication attempts.
* Flags IP addresses with three or more failures.
* Generates a basic login security report.

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

* Reads and analyses login records from a text file.
* Tracks successful and failed login attempts.
* Identifies invalid log entries.
* Monitors repeated failed attempts by IP address.
* Flags suspicious login activity.
* Generates a basic security analysis report.

08. IP Address Validator

* Validates IPv4 and IPv6 addresses.
* Identifies address types using Python’s ipaddress module.
* * Classifies addresses as private, public, or special-purpose.
* Handles invalid input using exception handling.

09. Suspicious URL Checker

* Checks URLs for potentially suspicious characteristics.
* Uses basic rules to identify possible risks.

10. File Metadata Inspector

* Extracts basic file metadata using Python’s os module.
* Displays file name, extension, size, and timestamps.
* Identifies the estimated MIME type using mimetypes.
* Calculates the file’s SHA-256 hash.
* Generates a simple file metadata report.

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

