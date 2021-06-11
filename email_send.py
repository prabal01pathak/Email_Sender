import os
import smtplib 
from email.message import EmailMessage
import imghdr
from pathlib import Path

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')
contacts = [EMAIL_ADDRESS , 'prabal0100pathak']
msg = EmailMessage()
msg['Subject'] = 'Grab dinner this weekend?'
msg['To']  = contacts
msg['From'] = EMAIL_ADDRESS
msg.set_content('How about dinner at 5pm this saturday?')
path = Path('C:\\Users\\hp\\Downloads\\wp.jpg')
with open(path,'rb') as apple:
    file_data  = apple.read()
    file_type  = imghdr.what(apple.name)
    file_name  = path.stem


msg.add_attachment(file_data,maintype = 'image',subtype = file_type ,filename = file_name)


print('sending..')
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS ,EMAIL_PASSWORD)

    smtp.send_message(msg)
    print('done')

