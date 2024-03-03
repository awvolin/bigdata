import requests

class Access:
    '''Access class for interacting with Spotify API'''

    def __init__(self):
        '''Initialize Access class'''
        self.CLIENT_ID = '412ebba147bc479483eae878c4191a3e'
        self.CLIENT_SECRET = '32a4a345fcdc4ab58e2a4b57d709818d'
        self.AUTH_URL = 'https://accounts.spotify.com/api/token'

        auth_response = requests.post(self.AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
        })

        auth_response_data = auth_response.json()
        self.access_token = auth_response_data['access_token']

        self.headers = {
            'Authorization': 'Bearer {token}'.format(token=self.access_token)
        }

        self.BASE_URL = 'https://api.spotify.com/v1/'

    def albumByArtist(self, artist_id):
        '''Get all albums by a given artist'''
        r = requests.get(self.BASE_URL + 'artists/' + artist_id + '/albums',
                         headers=self.headers,
                         params={'include_groups': 'album', 'limit': 50})
        d = r.json()

        albums_data = []
        for album in d['items']:
            album_data = {
                'name': album['name'],
                'release_date': album['release_date'],
                'tracks': self.getTracksForAlbum(album['id'])
            }
            albums_data.append(album_data)
        return albums_data

    def getTracksForAlbum(self, album_id):
        '''Get all tracks for a given album'''
        r = requests.get(self.BASE_URL + 'albums/' + album_id + '/tracks',
                        headers=self.headers,
                        params={'limit': 50})
        tracks_data = r.json()

        tracks = []
        for track in tracks_data['items']:
            track_id = track['id']
            track_info = self.getTrack(track_id)
            if track_info:
                tracks.append(track_info)

        return tracks

    def getTrack(self, track_id):
        '''Get details of a track'''
        r = requests.get(self.BASE_URL + 'tracks/' + track_id,
                        headers=self.headers)
        track_data = r.json()

        if 'name' in track_data and 'artists' in track_data:
            track_info = {
                'name': track_data['name'],
                'artists': [artist['name'] for artist in track_data['artists']],
                'popularity': track_data.get('popularity', None),
                'runtime': track_data.get('duration_ms', None)
            }
            return track_info
        else:
            return None
