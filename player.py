#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
from dotenv import load_dotenv
import os
import json 

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
DEVICE_ID = os.getenv("DEVICE_ID")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = 'user-read-playback-state,user-modify-playback-state,playlist-read-private, playlist-read-collaborative,user-library-read'

with open('album_uri.json', 'r') as file:
    album_uri = json.load(file)

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                    client_secret=CLIENT_SECRET,
                                                    redirect_uri=REDIRECT_URI,
                                                    scope=SCOPE))
            
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id= reader.read()[0]
            print("Card Value is:",id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
                
            if id in album_uri:
                sp.start_playback(device_id=DEVICE_ID, context_uri=f'spotify:album:{album_uri[id]}')
                sleep(2)
            elif id == 1:
                sp.pause_playback(device_id=DEVICE_ID)
                sleep(2)
            elif id == 2:
                sp.start_playback(device_id=DEVICE_ID)
                sleep(2)
            elif id == 3:
                sp.previous_track(device_id=DEVICE_ID)
                sleep(2)
            elif id == 4:
                sp.next_track(device_id=DEVICE_ID)
                sleep(2)
            elif id == 5:
                sp.shuffle(state=True, device_id=DEVICE_ID)
                sleep(2)
            elif id == 6:
                sp.shuffle(state=False, device_id=DEVICE_ID) 
                sleep(2)           

    except Exception as e : 
        print(e)
        pass
    finally:
        print("Claening up....")
        GPIO.cleanup()





