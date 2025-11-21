import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
APP_PASSWORD = os.getenv('APP_PASSWORD') # Use the App Password, not your regular password


   
   
   
def send_gmail(mail,final_email_text):
    # 1. Create the email message object
     msg = EmailMessage()
     msg['Subject'] = "Daily Learning "
     msg['From'] = SENDER_EMAIL
     msg['To'] = mail
     msg.add_alternative(final_email_text, subtype="html")

    # 2. Connect to the Gmail SMTP server
    # The default secure port for SMTP over SSL/TLS is 465
     try:
        print("Attempting to connect to Gmail SMTP server...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            
            # 3. Log in to the server using the App Password
            server.login(SENDER_EMAIL, APP_PASSWORD)
            
            # 4. Send the email
            server.send_message(msg)
            
            print(f"✅ Success! Email sent to {mail}")
            
     except smtplib.SMTPAuthenticationError:
        print("❌ ERROR: SMTP Authentication Failed.")
        print("Please check your SENDER_EMAIL and ensure you are using the correct 16-digit APP_PASSWORD.")
     except Exception as e:
        print(f"❌ An error occurred: {e}")    
    
    
