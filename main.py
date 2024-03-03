import json
import matplotlib.pyplot as plt
from access import Access
from redis_access import Redis_Access

def main():
    access_instance = Access()
    redis_instance = Redis_Access()
    
    artist_id = '4dpARuHxo51G3z768sgnrY'  # Adele
    albums = access_instance.albumByArtist(artist_id)
    
    # Insert album data into Redis
    redis_instance.insert_album_data(artist_id, albums)
    
    # Retrieve album data from Redis
    key = artist_id
    album_data = redis_instance.getValues(key)
    
    if album_data:
        # Check if album data is a list
        if isinstance(album_data, list):
            # Initialize lists to store album names and average popularities
            album_names = []
            average_popularities = []
            total_runtimes = []
            
            # Loop through each album
            for album in album_data:
                # Extract track data from album data
                tracks = album['tracks']
                
                # Calculate average popularity
                total_popularity = sum(track['popularity'] for track in tracks)
                average_popularity = total_popularity / len(tracks)
                
                # Total runtime in minutes
                total_runtime = sum(track['runtime'] for track in tracks) / 100000

                most_popular_track = max(tracks, key=lambda x: x['popularity'])
                print(f"Most popular song on {album['name']}: {most_popular_track['name']} - {', '.join(most_popular_track['artists'])}")
                
                album_names.append(album['name'])
                average_popularities.append(average_popularity)

                total_runtimes.append(total_runtime)
            
            plt.bar(album_names, average_popularities)
            plt.xlabel('Album')
            plt.ylabel('Average Popularity')
            plt.title('Average Popularity of Songs on Each Album')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

            plt.bar(album_names, total_runtimes, color='orange')
            plt.xlabel('Album')
            plt.ylabel('Total Runtime (minutes)')
            plt.title('Total Runtime of Songs on Each Album')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
        else:
            print("No albums found.")
    else:
        print("Album data not found.")

if __name__ == "__main__":
    main()
