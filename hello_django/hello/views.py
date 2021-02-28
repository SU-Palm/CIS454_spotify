from django.shortcuts import render
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
#Spotify api
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#ends here

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

#def spotify():
    #sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,
                                               #client_secret="YOUR_APP_CLIENT_SECRET",
                                               #redirect_uri="YOUR_APP_REDIRECT_URI",
                                               #scope="user-library-read"))

    #esults = sp.current_user_saved_tracks()
    #for idx, item in enumerate(results['items']):
        #track = item['track']
        #print(idx, track['artists'][0]['name'], " – ", track['name'])
