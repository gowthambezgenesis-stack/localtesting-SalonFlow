import random
import logging
from django.conf import settings
from twilio.rest import Client

logger = logging.getLogger(__name__)

def generate_otp():
    """Generate 4 digit OTP"""
    otp = str(random.randint(1000, 9999))
    return otp
def send_otp(phone, otp):
    """
    Send OTP using Twilio SMS
    """
    try:
        # Initialize Twilio client
        client = Client(
            settings.TWILIO_ACCOUNT_SID,
            settings.TWILIO_AUTH_TOKEN
        )

        # Send SMS
        message = client.messages.create(
            body=f"Your SalonFlow OTP is: {otp}",
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone
        )

        logger.info(f"OTP sent successfully to {phone}")
        logger.info(f"Twilio SID: {message.sid}")

        return message.sid

    except Exception as e:
        logger.error(f"Failed to send OTP: {str(e)}")
        print(f"❌ Twilio Error: {e}")

        return None
