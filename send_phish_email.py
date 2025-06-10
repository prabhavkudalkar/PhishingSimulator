import yagmail

# --- Email Configuration (YOU MUST FILL THESE IN) ---
SENDER_EMAIL = "tes@test.net"  # Your Google Workspace email
SENDER_PASSWORD = "*******" # <-- THIS MUST BE THE GOOGLE APP PASSWORD

# The email address(es) of your target employee(s) for the simulation
TARGET_EMAILS = [" input target email "] # Your test targets

# The link to your running Flask server (use ngrok for external testing!)
PHISHING_LINK = "https://data.actionfraud.police.uk/cms/wp-content/uploads/2020/09/Phishing-attacks-dealing-with-suspicious-emails.pdf" # CHANGE THIS TO YOUR NGROK URL LATER!

# --- Phishing Email Content ---
SUBJECT = "Action Required: Verify Your Account"
DISPLAY_FROM = "Dad AI Internal Security <security@dad.net>"

# HTML content of the email
HTML_BODY = f"""
<html>
<body>
    <p>Dear Valued Employee,</p>
    <p>We've detected unusual activity on your Dad account. For your security, we require you to verify your account details immediately.</p>
    <p>Please click the link below to verify your account and prevent any service interruptions:</p>
    <p><a href="{PHISHING_LINK}">Verify Your Account Now</a></p>
    <p>Failure to do so may result in temporary suspension of your account access.</p>
    <p>Thank you for your cooperation.</p>
    <p>Sincerely,</p>
    <p>The Dad AI Security Team</p>
    <p style="font-size:10px; color:#aaa;">This is an automated message. Please do not reply.</p>
</body>
</html>
"""

def send_phishing_email_yagmail(target_email_address):
    try:
        # Initialize yagmail with your sender credentials
        yag = yagmail.SMTP(user=SENDER_EMAIL, password=SENDER_PASSWORD)

        # Send the email
        yag.send(
            to=target_email_address,
            subject=SUBJECT,
            contents=HTML_BODY,
            # Set the 'From' header to make it look legitimate
            headers={'From': DISPLAY_FROM}
        )
        print(f"[*] Phishing email sent successfully to {target_email_address} using yagmail.")

    except yagmail.YagAuthenticationError:
        print(f"[-] Failed to send email to {target_email_address}: Yagmail Authentication error. Check SENDER_EMAIL and SENDER_PASSWORD (App Password).")
    except Exception as e:
        print(f"[-] An unexpected error occurred while sending to {target_email_address} using yagmail: {e}")

if __name__ == "__main__":
    print("Starting email sending process with yagmail...")
    for target_email in TARGET_EMAILS:
        send_phishing_email_yagmail(target_email)
    print("Email sending process complete.")