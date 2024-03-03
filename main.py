from access import Access
from redis_access import RedisAccess

def main():
    access_instance = Access()
    redis_instance = RedisAccess()
    artist_id = '4dpARuHxo51G3z768sgnrY'  # Adele
    albums = access_instance.albumByArtist(artist_id)
    
    # Loop through albums and print track info
    for album in albums:
        print("Album:", album['name'], "-", album['release_date'])
        print("Tracks:")
        for idx, track in enumerate(album['tracks'], start=1):
            print(f"\t{idx}. {track['name']} - {', '.join(track['artists'])}")

    # Insert album data into Redis
    redis_instance.insert_album_data(artist_id, albums)

if __name__ == "__main__":
    main()
