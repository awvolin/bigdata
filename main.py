# main.py
from access import Access

def main():
    access_instance = Access()
    artist_id = '4dpARuHxo51G3z768sgnrY'        #Adele
    access_instance.albumByArtist(artist_id)

if __name__ == "__main__":
    main()
