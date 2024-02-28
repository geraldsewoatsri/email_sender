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

emails_list = emails.splitlines()

# Reading the message from txt file
file_message = open('message.txt', 'r')
message = file_message.read()
file_message.close()


def send_email_now():
    msg['From'] = smtp_username
    msg["Subject"] = "Enter your subject here."
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
    
    sent_emails = 0
    try:
        for email in emails_list:
            msg['To'] = email
            smtp_server.sendmail(msg['From'], msg['To'], msg.as_string())
            sent_emails +=1
            time.sleep(3)
            if sent_emails >= len(emails):
                print("All emails have been sent successfully")
    except Exception as e:
        print("An error occured while sending your email", e)
    finally:
        smtp_server.quit()
    return True
    
    #try:
        #smtp_server.sendmail(msg['From'], msg['To'], message)
        #smtp_server.send_message(msg)
    


if __name__ == "__main__":
    send_email_now()