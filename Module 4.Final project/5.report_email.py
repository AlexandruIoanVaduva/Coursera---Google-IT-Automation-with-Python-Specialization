#!/usr/bin/env python3
import os, sys
import datetime
import reports
import emails
from reports import generate_report
from emails import send_email, generate_email

file_list = [f for f in os.listdir("supplier-data/descriptions") if ".txt" in f]
dict = {"name": [], "weight": []}

for y in file_list:
    with open("supplier-data/descriptions/" + y) as x:
        lines = [line.rstrip('\n') for line in x]
    dict["name"].append(lines[0])
    dict["weight"].append(lines[1])

fruits = []

for i in range(len(dict['weight'])):
    fruit = f"name: {dict['name'][i]}\nweight: {dict['weight'][i]}\n"
    fruits.append(fruit)

text = "\n".join(fruits)

def main(argv):
    file_path = "/tmp/processed.pdf"
    today = datetime.date.today()
    title = "Processed Update on " + today.strftime("%B %d, %Y")
    paragraph = text.replace('\n', '<br />\n')
    reports.generate_report(file_path, title, paragraph)
    sender = "automation@example.com"
    recipient = "student@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, recipient, subject, body, file_path)
    emails.send_email(message)

if __name__ == "__main__":
    main(sys.argv)
