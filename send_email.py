"""Sending mail is done with Python's smtplib using an SMTP (Simple Mail Transfer Protocol) server. Actual usage
varies depending on complexity of the email and settings of the email server, we'll send email through Google's Gmail.
To include a From, To and Subject headers, we should use the email package, since smtplib does not modify the
contents or headers at all."""

import smtplib, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# headers
me = input("Enter your email: ")
pswd = input("Enter your password (note that it'll be visible while you type): ")
receiver = input("Enter the receiver's email: ")
msg = MIMEMultipart()
msg["From"] = me
msg["To"] = receiver
msg["Subject"] = input("Enter the subject: ")

# body
body = input("Enter your message:\n")
msg.attach(MIMEText(body, 'plain'))

# server
confirm = input("Enter 'y' to send message: ")
mail_server = "smtp.gmail.com"  # for outlook: 'smtp-mail.outlook.com'
print("Processing...")

if confirm == 'y':
    server = smtplib.SMTP(mail_server, 587)  # port
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(me, pswd)
    response = server.sendmail(me, receiver, msg.as_string())
    if response != {}:
        print("\nSending failed for ", response)
    else:
        print("\nMessage successfully sent.")
else:
    print("\nNOT sent!")

