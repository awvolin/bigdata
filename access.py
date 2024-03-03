# access.py
import requests

class Access:
    def __init__(self):
        self.CLIENT_ID = '412ebba147bc479483eae878c4191a3e'
        self.CLIENT_SECRET = '32a4a345fcdc4ab58e2a4b57d709818d'
        self.AUTH_URL = 'https://accounts.spotify.com/api/token'

        # POST
        auth_response = requests.post(self.AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
        })

        # convert the response to JSON
        auth_response_data = auth_response.json()

        # save the access token
        self.access_token = auth_response_data['access_token']

        self.headers = {
            'Authorization': 'Bearer {token}'.format(token=self.access_token)
        }

        # base URL of all Spotify API endpoints
        self.BASE_URL = 'https://api.spotify.com/v1/'

    def albumByArtist(self, artist_id):
        # pull all artist's albums
        r = requests.get(self.BASE_URL + 'artists/' + artist_id + '/albums',
                         headers=self.headers,
                         params={'include_groups': 'album', 'limit': 50})
        d = r.json()

        for album in d['items']:
            print(album['name'], ' --- ', album['release_date'])
