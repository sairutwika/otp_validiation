import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import time

otp = random.randint(1111,9999)
otp_generation_time = time.time()

smtp_server = "smtp.gmail.com"
smtp_port = 587

username = "sairutwika1408@gmail.com"
password = "xxxx xxxx xxxx xxxx"

from_email = "sairutwika1408@gmail.com"
to_email = input("Enter email to send OTP: ")
subject = "OTP validation"
body = f"OTP for Validation is {otp}. \nDont share your OTP\nThank You"


msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.login(username,password)
server.send_message(msg)
server.quit()
print("email sent")
for i in range(2):
    if time.time() - otp_generation_time>300:
        print("OTP has expired.Request a new one.")
        break
    x = int(input("Enter OTP recived to your mail:"))
    print("Dont Share your OTP")
    if ( x == otp):
        print("valid")
        
        break
    else:
        print("OTP IS NOT Invalid")

        
        
else:
    print("invalid, NO option Left")
    print("Thank you")
    

    
