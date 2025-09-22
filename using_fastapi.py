from fastapi import FastAPI, HTTPException, Form
from pydantic import EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI()

# Your Gmail credentials (use an app password, NOT your normal password)
GMAIL_USER = "your_email@gmail.com"
GMAIL_APP_PASSWORD = "your_16_char_app_password"

@app.post("/send-email/")
async def send_email(
    to_email: EmailStr = Form(...),
    subject: str = Form(...),
    body: str = Form(...)
):
    try:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.send_message(msg)
        server.quit()

        return {"message": "Email sent successfully"}

    except smtplib.SMTPAuthenticationError:
        raise HTTPException(status_code=401, detail="Authentication failed. Check your email and app password.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")
