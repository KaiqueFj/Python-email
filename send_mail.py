import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Kaique Ferraz'
email['to'] = 'kaiquelferraz@hotmail.com'
email['subject'] = 'You were selected to the nba draft!'

email.set_content(html.substitute({'name': 'Kaique'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('kaiqueteste26@gmail.com', 'KaiqueTNT4321')
    smtp.send_message(email)
    print('all good boss!')
