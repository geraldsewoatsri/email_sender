import smtplib
from email.message import EmailMessage
import time


msg = EmailMessage()   #msg is an object created from EmailMessage() class

# Your smtp credentials here
smtp_username = 'payslyde@gmail.com'
stmp_password = 'huwhsspgmvwqciuq'


# Reading contacts from text file
file_contact = open('emails.txt', 'r')
emails = file_contact.read()
file_contact.close()

#emails_list = emails.splitlines()

# Reading the message from txt file
file_message = open('message.txt', 'r')
message = file_message.read()
file_message.close()


def send_email_now():
    msg['From'] = smtp_username
    msg["Subject"] = "Enter your subject here."
    msg['To'] = ", ".join(emails.splitlines())
    msg.set_content(message)
    
    # Authenticating gmail smtp
    smtp_server = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
    smtp_server.starttls()
    
    try:
        smtp_server.login('payslyde@gmail.com', 'huwhsspgmvwqciuq')
    except smtplib.SMTPAuthenticationError as e:
        print(e)
        print("SMTP credentials are invalid")
        return False
    
    try:
        #smtp_server.sendmail(msg['From'], msg['To'], message)
        smtp_server.send_message(msg)
    except Exception as e:
        print("An error occured while sending your email")
    finally:
        smtp_server.quit()
    return True


if __name__ == "__main__":
    send_email_now()