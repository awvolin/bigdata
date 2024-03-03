import json
import matplotlib.pyplot as plt
from access import Access
from redis_access import Redis_Access

def main():
    '''Main function to retrieve album data and visualize it'''
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
            # Initialize lists to store album names, average popularities, and total runtimes
            album_names = []
            average_popularities = []
            total_runtimes = []
            most_popular_songs = []

            # Loop through each album
            for album in album_data:
                # Extract track data from album data
                tracks = album['tracks']
                
                # Calculate average popularity
                total_popularity = sum(track['popularity'] for track in tracks)
                average_popularity = total_popularity / len(tracks)
                
                # Total runtime in minutes
                total_runtime = sum(track['runtime'] for track in tracks) / 100000

                # Find most popular song
                most_popular_track = max(tracks, key=lambda x: x['popularity'])
                most_popular_songs.append(most_popular_track['name'])

                # Append data to respective lists
                album_names.append(album['name'])
                average_popularities.append(average_popularity)
                total_runtimes.append(total_runtime)
            
            # Plotting average popularity and total runtime in a double bar graph
            fig, ax1 = plt.subplots()

            color = 'tab:red'
            ax1.set_xlabel('Album')
            ax1.set_ylabel('Average Popularity', color=color)
            ax1.bar(album_names, average_popularities, color=color)
            ax1.tick_params(axis='y', labelcolor=color)

            ax2 = ax1.twinx()  
            color = 'tab:blue'
            ax2.set_ylabel('Total Runtime (minutes)', color=color)
            ax2.bar(album_names, total_runtimes, color=color)
            ax2.tick_params(axis='y', labelcolor=color)

            fig.tight_layout()  
            plt.title('Average Popularity and Total Runtime of Songs on Each Album')
            plt.xticks(rotation=45, ha='right')
            plt.show()

            # Print most popular song on each album
            for i, album_name in enumerate(album_names):
                print(f"Most popular song on {album_name}: {most_popular_songs[i]}")

        else:
            print("No albums found.")
    else:
        print("Album data not found.")

if __name__ == "__main__":
    main()
