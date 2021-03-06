import os
import smtplib 
from email.message import EmailMessage
import imghdr
from pathlib import Path


EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')
Reciver = os.getenv("REC_EMAIL")
Paths = os.getenv('Paths')
contacts = [EMAIL_ADDRESS,Reciver]
msg = EmailMessage()
msg['Subject'] = 'How to send mail'
msg['To'] = contacts
msg['From'] = EMAIL_ADDRESS 
msg1 = EmailMessage()
msg1['Subject'] = 'Grab dinner this weekend?'
msg1['To']  = contacts
msg1['From'] = EMAIL_ADDRESS
msg1.set_content('How about dinner at 5pm this saturday?')
path = Path(Paths)
with open(path,'rb') as resume:
    file_data  = resume.read()
    file_name  = path.parts[-1]


msg1.add_attachment(file_data,maintype = 'pdf',subtype = 'pdf' ,filename = file_name)

print('sending..')
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS ,EMAIL_PASSWORD)

    smtp.send_message(msg1)
    print('done')
