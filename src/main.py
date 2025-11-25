from api.fetch import fetch_recently_played, fetch_top_artists, fetch_top_tracks

def main():
    print("Obteniendo datos del usuario")
    
    tracks= fetch_top_tracks(limit=25)
    artists = fetch_top_artists(limit=50)
    recent = fetch_recently_played(limit=10)
    
    print("\n TOP 25 CANCIONES:")
    for n,t in enumerate(tracks["items"], 1):
        print(f"{n} - {t["name"]} , by {t["artists"][0]["name"]}")
        
    print("\n TOP 50 ARTISTAS VARIOS AÑOS:")
    for n,a in enumerate(artists["items"], 1):
        print(f"{n} - {a["name"]}")
        
    
    print("\n CANCIONES RECIENTES:")
    for item in recent["items"]:
        track = item["track"]
        print(f"- {track["name"]} by {track["artists"][0]["name"]}")
        
if __name__ == "__main__":
    main()
    