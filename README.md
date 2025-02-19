# otp_validiation

Description

This project implements an OTP (One-Time Password) validation system using Python's smtplib for sending emails. The script generates a random OTP and sends it to the user's email address. The user is then prompted to enter the received OTP for validation. The system allows up to two attempts before locking the user out.

#Features

Generates a random 4-digit OTP.

Sends OTP via email using Gmail's SMTP server.

User validation with a maximum of two attempts.

Secure communication using TLS encryption.

#Prerequisites

Before running this project, ensure you have:

Python installed (>=3.6 recommended)

An active Gmail account

Enabled "Less Secure Apps" access or generated an App Password for Gmail (Recommended for security)
