from .auth import get_spotify_client

def get_client():
    try:
        import spotipy
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            "Missing dependency 'spotipy'. Please install it with: pip install spotipy"
        ) from e
    return spotipy.Spotify(auth_manager=get_spotify_client())

def fetch_top_tracks(limit= 100, time_range ="medium_term"):
    sp = get_client()
    return sp.current_user_top_tracks(limit=limit, time_range=time_range)

def fetch_top_artists(limit = 50, time_range="medium_term"):
    sp = get_client()
    return sp.current_user_top_artists(limit=limit, time_range=time_range)

def fetch_recently_played(limit =50):
    sp = get_client()
    return sp.current_user_recently_played(limit=limit)
