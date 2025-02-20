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
CACHE_PATH = os.getenv("CACHE_PATH")

with open('album_uri.json', 'r') as file:
    album_uri = json.load(file)

with open('playlist_uri.json', 'r') as file:
    playlist_uri = json.load(file)

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
                

            #code for playlists 
            if str(id) in playlist_uri:
                sp.start_playback(device_id=DEVICE_ID, context_uri=f"spotify:playlist:{playlist_uri[str(id)]}")
                sleep(2)

            #code for playlists
            if str(id) in album_uri:
                sp.start_playback(device_id=DEVICE_ID, context_uri=f'spotify:album:{album_uri[str(id)]}')
                sleep(2)
                
            playback_state = sp.current_playback()
            if playback_state is not None:
                if id == 694690578903:
                    shuffle_state = playback_state['shuffle_state']
                    if shuffle_state: 
                        sp.shuffle(False, device_id=DEVICE_ID)
                    else:
                        sp.shuffle(True, device_id=DEVICE_ID)
                        
                if id== 635651817888 :
                    is_playing = playback_state['is_playing']
                    if is_playing:
                        sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
                    else:
                        sp.start_playback(device_id=DEVICE_ID)
            else:
                print("No playback detected.") 


            if id == 66895890293:
                sp.next_track(device_id=DEVICE_ID)

            if id == 364670485943:
                sp.previous_track(device_id=DEVICE_ID)


    except Exception as e : 
        print(e)
        pass
    finally:
        print("Claening up....")
        GPIO.cleanup()
