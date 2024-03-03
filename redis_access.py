# redis_access.py
import redis
import json

class RedisAccess:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)

    def insert_album_data(self, artist_id, albums_data):
        # Convert albums data to JSON string
        albums_json = json.dumps(albums_data)
        
        # Insert JSON data into Redis
        self.redis_client.set(artist_id, albums_json)
        print("Album data inserted into Redis successfully.")
