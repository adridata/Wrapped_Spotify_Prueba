import json
import os

def load_config():
    # Resolve project root relative to this file (src/api -> project root)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
    path = os.path.join(project_root, "config", "config.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found at {path}. Expected a config/config.json in the project root.")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def get_spotify_client():
    cfg = load_config()
    # import spotipy locally to avoid requiring it when simply reading config
    try:
        from spotipy.oauth2 import SpotifyOAuth
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            "Missing dependency 'spotipy'. Please install it with: pip install spotipy"
        ) from e

    # spotify oauth uses `scope` (singular) argument; config uses `scopes` key
    auth = SpotifyOAuth(
        client_id=cfg.get("client_id"),
        client_secret=cfg.get("client_secret"),
        redirect_uri=cfg.get("redirect_uri"),
        scope=cfg.get("scopes")
    )
    return auth