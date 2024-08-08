import smtplib 
from email.message import EmailMessage

msg = EmailMessage()

msg.set_content("A la mesure de l'espace l'esprit, à la mesure de l'esprit, l'espace")
msg['Subject'] = "Hahaha"
msg['from'] = 'dev@debian.testing'
msg['to'] = 'timine2764@almaxen.com'

session = smtplib.SMTP("localhost")
# session.login('dev@debian.testing', '')
session.send_message(msg, 'dev@debian.testing', 'timine2764@almaxen.com')
session.quit()
