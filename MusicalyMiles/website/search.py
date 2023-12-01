import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def generate_playlist(artist_name):
    # Your Spotify API credentials
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'

    # Authenticate with Spotify API
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Search for the artist
    results = sp.search(q=artist_name, type='artist', limit=1)
    if not results['artists']['items']:
        print(f"Artist '{artist_name}' not found on Spotify.")
        return

    artist_id = results['artists']['items'][0]['id']

    # Get top tracks by the artist
    top_tracks = sp.artist_top_tracks(artist_id)

    # Create a playlist and add top tracks to it
    playlist_name = f"{artist_name} Top Tracks"
    playlist_description = f"Top tracks by {artist_name} on Spotify"

    playlist = sp.user_playlist_create(sp.me()['id'], playlist_name, public=True, description=playlist_description)

    track_uris = [track['uri'] for track in top_tracks['tracks']]
    sp.playlist_add_items(playlist['id'], track_uris)

    print(f"Playlist '{playlist_name}' created successfully!")

if __name__ == "__main__":
    artist_name = input("Enter the name of the artist: ")
    generate_playlist(artist_name)
