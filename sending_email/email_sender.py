import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv('C:/Users/KOOLKOOBO\Desktop/scripts/sending_email/.env')
email = EmailMessage()
email['from'] = 'Shakura Babanla'
email['to'] = 'emmanueladjerry@gmail.com'
email['subject'] = 'You just got your first $1,000,000'

email.set_content('You are now a millionaire')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(os.getenv('USERNAME'),os.getenv('PASSWORD') )
    smtp.send_message(email)
    print('you did well boss')