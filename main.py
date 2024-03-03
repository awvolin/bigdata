import requests

class main:

    CLIENT_ID = '412ebba147bc479483eae878c4191a3e'
    CLIENT_SECRET = '32a4a345fcdc4ab58e2a4b57d709818d'

    AUTH_URL = 'https://accounts.spotify.com/api/token'

    # POST
    auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    # base URL of all Spotify API endpoints 
    BASE_URL = 'https://api.spotify.com/v1/'

    # Track ID from the URI
    artist_id = '36QJpDe2go2KgaRleHCDTp'

    # pull all artists albums
    r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums', 
                    headers=headers, 
                    params={'include_groups': 'album', 'limit': 50})
    d = r.json()

    for album in d['items']:
        print(album['name'], ' --- ', album['release_date'])
