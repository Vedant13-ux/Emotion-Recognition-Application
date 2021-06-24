import smtplib

def send_email(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    # Authentication
    s.login("xyz@gmail.com", '**************')

    # message to be sent

    # sending the mail
    s.sendmail("xyz@gmail.com", "abc@gmail.com", message)

    # terminating the session
    s.quit()