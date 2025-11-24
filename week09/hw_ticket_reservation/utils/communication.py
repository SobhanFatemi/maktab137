import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
        from_email = 'sobhanfatemi56@gmail.com'
        password = 'oeajznbjrxtxfmme'

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, password)
            server.send_message(msg)
            print(f"OTP sent to '{to_email}'!")