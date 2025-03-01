#!/usr/bin/env python
#script to read rfid tag id's 
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        print("Waiting for you to scan an RFID sticker/card")
        id = reader.read()[0]
        print("The ID for this card is:", id)
        
finally:
        GPIO.cleanup()