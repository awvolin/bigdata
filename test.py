import redis

# Connect to Redis
r = redis.Redis(
    host='redis-14211.c251.east-us-mz.azure.cloud.redislabs.com',
    port=14211,
    password='KGEZypz9ZIucVISoWp9IEijHOKjsjTO2',
    decode_responses=True  # This ensures that retrieved values are decoded into Python strings
)

# Print everything in the database
keys = r.keys()  # Get all keys
for key in keys:
    value = r.get(key)  # Get value corresponding to the key
    print(f'{key}: {value}')

# Add something to the database
r.set('new_key', 'new_value')

# Print again to see the updated database
print("\nAfter adding 'new_key':")
keys = r.keys()  # Get all keys
for key in keys:
    value = r.get(key)  # Get value corresponding to the key
    print(f'{key}: {value}')
