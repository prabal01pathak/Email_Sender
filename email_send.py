import os
import smtplib 
from email.message import EmailMessage
import imghdr
from pathlib import Path


EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')
contacts = [EMAIL_ADDRESS , 'prabal0100pathak']
msg = EmailMessage()
msg['Subject'] = 'How to send mail'
msg['To'] = contacts
msg['From'] = EMAIL_ADDRESS 
msg1 = EmailMessage()
msg1['Subject'] = 'Grab dinner this weekend?'
msg1['To']  = contacts
msg1['From'] = EMAIL_ADDRESS
msg1.set_content('How about dinner at 5pm this saturday?')
path = Path('C:\\Users\\hp\\web\\files\\themes\\red\\new_resume.pdf')
with open(path,'rb') as apple:
    file_data  = apple.read()
    file_type  = imghdr.what(apple.name)
    file_name  = path.stem




print('sending..')
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS ,EMAIL_PASSWORD)

    smtp.send_message(msg1)
    print('done')

