import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import json 


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

album_uri = dict()

# Pagination variables
limit = 50  # Number of items to fetch per request
offset = 0  # Starting point for the next request
has_more = True  # Flag to check if there are more items to fetch

while has_more:
    # Fetch saved albums with the current offset and limit
    saved_albums = sp.current_user_saved_albums(limit=limit, offset=offset)
    
    # Check if there are any items in the response
    if not saved_albums["items"]:
        has_more = False
        break
    
    # Process each album in the current batch
    for item in saved_albums["items"]:
        album_info = item["album"]
        name = album_info["name"]
        uri = album_info["id"]
        album_uri[name] = uri
    
    # Update the offset for the next request
    offset += limit

# Print the number of albums fetched
print(f"Fetched {len(album_uri)} albums.")

with open('album_uri.json', 'w') as f: 
     f.write(json.dumps(album_uri, indent=4))