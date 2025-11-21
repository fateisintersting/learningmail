import csv
import os
import markdown2
import usersmail
from premailer import transform
# Define the file path
file_path = 'emailslist.csv'


def convert_and_style(text):
    body_html = markdown2.markdown(text)

    template = f"""
    <html>
    <body style="font-family: Arial; background:#f4f4f4; padding:20px;">
        <div style="max-width:600px; margin:auto; background:white; padding:20px; border-radius:10px;">
            {body_html}
        </div>
    </body>
    </html>
    """

    return transform(template)  # makes CSS email-safe



# Check if the file exists before trying to open it
def sendingMails(final_email_text):
    if not os.path.exists(file_path):
     print(f"❌ Error: The file '{file_path}' was not found. Please create it first.")
    else:
     print(f"✅ Reading emails from '{file_path}'...")
    
    # Use a 'with' statement for file handling to ensure it closes properly
    html_body = markdown2.markdown(final_email_text)
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            
            # Use csv.reader or csv.DictReader. DictReader is usually better
            # because it uses the header row (Name, Email) as keys.
            reader = csv.DictReader(file)
            htmeamilbody = convert_and_style(final_email_text)
            
            # Start looping through each row in the CSV file
            for row in reader:
                
                # The 'row' is a dictionary where keys are the column headers
                name = row['Name']
                email = row['Email']
                
                print(f"--- Processing Email ---")
                print(f"Name: {name}")
                print(f"Email: {email}")
                usersmail.send_gmail(email,htmeamilbody)
                
                # --- ACTION LOOP ---
                # This is where you would integrate an action, such as:
                # 1. Sending an email using the smtplib module
                # 2. Saving the email to a database
                # 3. Performing data validation on the email address
                
                # Example Action: Print a mock action
                print(f"Action: Preparing to send personalized email to {name} at {email}...")
            
            print("---")
            print("✅ Finished looping through all emails.")

    except Exception as e:
        print(f"❌ An error occurred during file reading: {e}")