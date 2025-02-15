import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import json 
import requests
import re

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
DEVICE_ID = os.getenv("DEVICE_ID")
REDIRECT_URI = os.getenv("REDIRECT_URI")

SCOPE = 'user-read-playback-state,user-modify-playback-state,playlist-read-private, playlist-read-collaborative,user-library-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
    ))


playlist_uri = dict()
pattern = r'[<>:"/\\|?*]'

# Pagination variables
limit = 50  # Number of items to fetch per request
offset = 0  # Starting point for the next request
has_more = True  # Flag to check if there are more items to fetch

while has_more:
    # Fetch saved albums with the current offset and limit
    playlists = sp.current_user_playlists(limit=limit, offset=offset)
    # Check if there are any items in the response
    if not playlists["items"]:
        has_more = False
        break
    
    # Process each album in the current batch
    for item in playlists["items"]:
        name = item["name"]
        uri = item["id"]
        image_url = item["images"][0]["url"]
        playlist_uri[name] = uri
        '''
        response = requests.get(image_url)
        if response.status_code == 200:
             # Clean the album name for use as a filename
            filename = re.sub(pattern, "", name)
            
            # Save the image
            with open(fr"{directory}/{filename}.jpg", 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download image for playlist: {name}")
        '''
        
    # Update the offset for the next request
    offset += limit

# Print the number of albums fetched
print(f"Fetched {len(playlist_uri)} playlists.")



with open('playlist_uri.json', 'w') as f: 
     f.write(json.dumps(playlist_uri, indent=4))

