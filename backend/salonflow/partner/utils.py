import random
from twilio.rest import Client
import os

def generate_otp():
    return str(random.randint(1000, 9999))


def send_otp(phone, otp):
    try:
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        twilio_number = os.getenv("TWILIO_PHONE_NUMBER")

        if not all([account_sid, auth_token, twilio_number]):
            raise ValueError("Twilio environment variables are missing")

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"Your OTP is {otp}",
            from_=twilio_number,
            to=phone
        )

        print("OTP sent successfully:", message.sid)
        return message.sid

    except Exception as e:
        print("Twilio SMS failed:", str(e))
        return None
