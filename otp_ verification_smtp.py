import math
import random
import smtplib
from email.mime.text import MIMEText

# Generate a 6-digit OTP
digits = "0123456789"
OTP = "".join(random.choice(digits) for _ in range(6))

# Email message
msg = f"{OTP} is your OTP."

# Email sender credentials
sender_email = "your-email@gmail.com"
app_password = "your-app-password"

# Set up SMTP server
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)

    # Get recipient email
    recipient_email = input("Enter your email: ")

    # Create email message
    email_message = MIMEText(msg)
    email_message["From"] = sender_email
    email_message["To"] = recipient_email
    email_message["Subject"] = "Your OTP Verification Code"

    # Send email
    server.sendmail(sender_email, recipient_email, email_message.as_string())
    server.quit()

    # OTP verification
    user_otp = input("Enter Your OTP >>: ")
    if user_otp == OTP:
        print("Verified")
    else:
        print("Please check your OTP again.")

except Exception as e:
    print(f"Error: {e}")