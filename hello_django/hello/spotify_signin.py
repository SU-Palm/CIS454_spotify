import spotipy # Spotify api
from spotipy import SpotifyOAuth
from spotipy.cache_handler import CacheHandler
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOauthError
import os # Fetches enviroment variables

client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')

def spotify_auth():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
                                                   client_secret,
                                                   redirect_uri="http://127.0.0.1:8008",
                                                   scope="user-library-read"))

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
