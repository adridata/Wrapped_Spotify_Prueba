import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

with open("config/config.json") as f:
    cfg = json.load(f)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=cfg["client_id"],
        client_secret=cfg["client_secret"],
        redirect_uri=cfg["redirect_uri"],
        scope=cfg["scopes"]
    )
)

me = sp.current_user()
print("Estas logueado como:", me["display_name"])
