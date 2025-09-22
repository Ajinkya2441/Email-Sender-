import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    try:
        # For Gmail, use smtp.gmail.com and port 587
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

# Usage example:
if __name__ == "__main__":
    sender = "pagareajinkya24@gmail.com"
    password = "Vicky@24."
    recipient = "pagareajinkya04@example.com"
    subject = "Test Email from Python"
    body = "Hello! This is a test email sent from a Python script."

    send_email(sender, password, recipient, subject, body)
