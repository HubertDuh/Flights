import requests
from api.config import settings

ROOT_URL = settings.ROOT_URL

def states_accessor():
    # go through the doc API exampls!

    url = f"{ROOT_URL}/states/all"
    r = requests.get(url)
    if not r.ok:    # seeing if the response (Error 404 for example) is 200 aka ok
        raise RuntimeError(r.json())
    print(r.json())

def tracks_accessor():

    # Doesn't work anymore

    url = f"{ROOT_URL}/tracks/all?icao24=3c4b26&time=0"
    r = requests.get(url)
    if not r.ok:  # seeing if the response (Error 404 for example) is 200 aka ok
        raise RuntimeError(r.json())
    print(r.json())



