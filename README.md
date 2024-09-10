# SIRS Project

## Overview

The SIRS (Security Incident Response System) Project is a Python-based application designed to assist with managing and responding to security incidents. The script reads Windows Event Logs, stores relevant incident data in a SQLite database, generates a detailed report, and sends it via email.

## Features

- **Reads Windows Event Logs**: Extracts security-related events.
- **Stores Data**: Saves event data in a SQLite database.
- **Generates Report**: Creates a summary of incidents and stores it in a text file.
- **Email Notification**: Sends an email with the report attached.

## Requirements

- **Python 3.x**: Ensure you have Python 3 installed.
- **Python Libraries**:
  - `pandas`: For data manipulation and analysis.
  - `sqlite3`: For database operations (included with Python).
  - `logging`: For logging events and errors.
  - `smtplib` and `email`: For sending emails.

## Installation

1. **Clone the Repository:**

   Open a terminal (Command Prompt or PowerShell) and navigate to your Desktop:
   ```sh
   cd C:\Users\Damian\Desktop
