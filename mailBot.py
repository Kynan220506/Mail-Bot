import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
RECIEVERS = os.environ.get('RECIEVERS_EMAIL')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    EMAIL_ADDRESS = input("Sender's Email Address: ")
    EMAIL_PASSWORD = input("Sender's Email Password: ")
    RECIEVERS = input("Reciever's Email Address: ")

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = input('Write Subject of E-Mail: ')
    body = input('Write Body of E-Mail: ')

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, RECIEVERS, msg)

    print("Sent Message.")