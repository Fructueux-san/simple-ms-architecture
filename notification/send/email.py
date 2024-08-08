import smtplib, os, json
from email.message import EmailMessage


def notification(message):
    try:
        message = json.loads(message)
        mp3_fid = message["mp3_fid"]
        sender_address = os.environ.get('EMAIL_ADDRESS')
        sender_password = os.environ.get('EMAIL_PASSWORD')
        receiver_address = message['username']

        msg = EmailMessage()
        msg.set_content(f"mp3 file_id:{mp3_fid} is now ready!")
        msg['Subject'] = "MP3 Download"
        msg['from'] = sender_address
        msg['to'] = receiver_address


        session = smtplib.SMTP("localhost")
        session.starttls()

        # My server doesn't support this login mechanos
        # session.login(sender_address, sender_password)
        session.send_message(msg, sender_address, receiver_address)
        session.quit()
        print("Mail sent")
    except Exception as err:
        print(err)
        return err
