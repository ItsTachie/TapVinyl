#script to get the album covers from spotify 

import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
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

images = dict()
directory = ""

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
        url = album_info["images"][0]["url"]
        images[name] = url
    
    # Update the offset for the next request
    offset += limit

# Print the number of albums fetched
print(f"Fetched {len(images)} albums.")

# Example: Save album covers to disk
import requests
import re

# Regular expression pattern to clean filenames
pattern = r'[<>:"/\\|?*]'

for album, cover_image in images.items():
    response = requests.get(cover_image)
    if response.status_code == 200:
        # Clean the album name for use as a filename
        clean_album_name = re.sub(pattern, "", album)
        
        # Save the image
        #replace directory with the appropriate folder to save the file to 
        with open(fr"{directory}{clean_album_name}.jpg", 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download image for album: {album}")

