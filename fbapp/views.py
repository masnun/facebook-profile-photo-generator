import facebook
import hashlib
import os
from PIL import Image

from django.http.response import HttpResponse
from django.shortcuts import render

DIMENSION = (480, 480)


def home(request):
    return render(request, "home.html")


def accounts_profile(request):
    # Get token
    social = request.user.social_auth.get(provider='facebook')
    token = social.extra_data['access_token']

    # Get photo
    client = facebook.GraphAPI(access_token=token, version='2.5')
    resp = client.request("/me/picture?width=480&height=480")

    # Store photo
    temp_file_name = "photos/" + hashlib.md5(token.encode('utf-8')).hexdigest() + ".jpg"

    try:
        file = open(temp_file_name, 'wb')
        file.write(resp['data'])

        background = Image.open(temp_file_name).resize(DIMENSION, Image.ANTIALIAS)
        foreground = Image.open("resources/badge.png").resize(DIMENSION, Image.ANTIALIAS)

        background.paste(foreground, (0, 0), foreground.convert('RGBA'))
        background.save(temp_file_name)

        response = HttpResponse(open(temp_file_name, "rb").read(), content_type="image/jpeg")

        os.unlink(temp_file_name)

        return response

    except:
        return HttpResponse("Sorry, an error occurred while generating your photo! Please retry later!")
