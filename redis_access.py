import json
import redis

class Redis_Access:
    def __init__(self):
        # Connect to Redis
        self.r = redis.Redis(
            host='redis-14211.c251.east-us-mz.azure.cloud.redislabs.com',
            port=14211,
            password='KGEZypz9ZIucVISoWp9IEijHOKjsjTO2',
            decode_responses=True  # This ensures that retrieved values are decoded into Python strings
        )
        
    def insert_album_data(self, artist_id, albums_data):
        
        # Clear database in testing
        self.r.flushdb()

        albums_json = json.dumps(albums_data)
        
        keys = self.r.keys() 
        for key in keys:
            value = self.r.get(key)  
            print(f'{key}: {value}')

        self.r.set(artist_id, albums_json)
        print("\nAfter adding 'new_key':")
        keys = self.r.keys() 
        for key in keys:
            value = self.r.get(key)  
            print(f'{key}:')
            print(json.dumps(json.loads(value), indent=4))  
            