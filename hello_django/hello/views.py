from django.shortcuts import render
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
#from hello import spotify_signin

def home(request):
    return render(
        request,
        'hello/signIn.html'
    )
    spotify_signin.spotify_auth()
    
# def hello_there(request, name):  Passing arguments through url
#     return render(
#         request,
#         'hello/signIn.html'
#     )
