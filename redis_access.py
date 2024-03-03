import json
import redis

class Redis_Access:
    '''Class for accessing Redis database'''

    def __init__(self):
        '''Initialize Redis connection'''
        self.r = redis.Redis(
            host='redis-14211.c251.east-us-mz.azure.cloud.redislabs.com',
            port=14211,
            password='KGEZypz9ZIucVISoWp9IEijHOKjsjTO2',
            decode_responses=True  # This ensures that retrieved values are decoded into Python strings
        )
        
    def insert_album_data(self, artist_id, albums_data):
        '''Insert album data into Redis'''
        # Clear database in testing
        self.r.flushdb()

        albums_json = json.dumps(albums_data)
        self.r.set(artist_id, albums_json)
        
    def getValues(self, key):
        '''Retrieve JSON value for the given key'''
        value = self.r.get(key)
        
        # If value exists, parse JSON and return
        if value:
            return json.loads(value)
        else:
            return None
