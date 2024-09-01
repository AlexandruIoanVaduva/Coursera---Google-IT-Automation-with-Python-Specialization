#!/usr/bin/env python3

import psutil
import socket
import emails
from emails import send_email, generate_email


subject_line = {"Case": ['CPU usage is over 80%', 'Available disk space is lower than 20%',
                         'available memory is less than 100MB',
                         'hostname "localhost" cannot be resolved to "127.0.0.1"'],
                "Subject line":["Error - CPU usage is over 80%", "Error - Available disk space is less than 20%",
                                "Error - Available memory is less than 100MB",
                                "Error - localhost cannot be resolved to 127.0.0.1"]}

print(subject_line["Case"])  # Output: CPU usage is over 80%
print(subject_line["Subject line"])

if psutil.cpu_percent() >= 80:
    subject = (subject_line["Subject line"][0])
elif psutil.disk_usage("/").percent >= 80:
    subject = (subject_line["Subject line"][1])
elif psutil.virtual_memory().available/ (1024 ** 2) < 100:
    subject = (subject_line["Subject line"][2])
elif socket.gethostbyname('localhost') == "127.0.0.1":
    print("localhost resolved to 127.0.0.1")
else:
    subject = (subject_line["Subject line"][3])

sender = "automation@example.com"
recipient = "student@example.com"
subject = "Upload Completed - Online Fruit Store"
body = "Please check your system and resolve the issue as soon as possible"
message = emails.generate_error_report(sender, recipient, subject, body)
emails.send_email(message)
