# Django
from django.core.exceptions import ImproperlyConfigured

# Third Party
from twilio.rest import TwilioRestClient
import RPi.GPIO as rasp_GPIO
import Adafruit_BBIO.GPIO as beagle_GPIO

# Python
import datetime
import os
import pytz

# Ours
from models import DoorTime

# BeagleBone IO
# GPIO2_6 - right P8 - 45
# GPIO2_27 - left P8 - 46

def detect():
    beagle_GPIO.add_event_detect("GPIO2_6", beagle_GPIO.FALLING)

def send():
    beagle_GPIO.setup("GPIO2_27", beagle_GPIO.OUT)
    beagle_GPIO.output("GPIO2_27", beagle_GPIO.HIGH)
    beagle_GPIO.cleanup()

def send_message(message, numbers=False):

    if not numbers:
        numbers = ["+6179812689"]
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    if not account_sid or not auth_token:
        raise ImproperlyConfigured("""
            There was no TWILIO_ACCOUNT_SID or TWILIO_AUTH_TOKEN found in the environment variables. \n
            Please set these variables.
            """)

    client = TwilioRestClient(account_sid, auth_token)
    
    message_list = []
    for number in numbers:
        message = client.messages.create(
            to=number, 
            from_="+16175002819",
            body=message,
        )
        message_list.append(message)

    return message_list

def create_valid_doortime(valid_time=False):

    if valid_time:
        doortime = DoorTime.objects.create(active_time=valid_time)
    else:
        doortime = DoorTime.objects.create()

    return doortime

def validate_doortime():

    door_check = DoorTime.objects.filter(active_time__lte=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC))

    return door_check.exists()