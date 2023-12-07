from flask import Blueprint, jsonify
"""from .models import YourModel  # import database models"""

from flask import request
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from singers import get_singer_by_state

api = Blueprint('api', __name__)

# Spotify API Constants and Functions
SPOTIFY_API_BASE_URL = "https://api.spotify.com/v1"

def get_spotify_access_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type: application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, headers = headers, data = data)
    if response.status_code == 200:
        return response.json().get["access_token"]
    return None

# fetch data from Spotify using the access token
def fetch_spotify_data(endpoint, token):
    url = f"https://api.spotify.com/v1/{endpoint}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response

#search for the "This Is {Artist Name}" playlist on Spotify and return
def get_artist_playlist(artist_name):
    # Get access token
    access_token = get_spotify_access_token(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    if not access_token:
        return None

    # Search for "This Is {Artist Name}" playlist
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    endpoint = "search"
    data = {"q": f"This Is {artist_name}", "type": "playlist", "limit": 1}
    response = fetch_spotify_data(f"{endpoint}?{urllib.parse.urlencode(data)}", access_token)
    if response.status_code != 200:
        return None

def get_artist_playlist(artist_name):
    # Get access token
    access_token = get_spotify_access_token(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    if not access_token:
        return None

    # Search for "This Is {Artist Name}" playlist
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    endpoint = "search"
    data = {"q": f"This Is {artist_name}", "type": "playlist", "limit": 1}
    response = fetch_spotify_data(f"{endpoint}?{urllib.parse.urlencode(data)}", access_token)
    if response.status_code != 200:
        return None

    playlist = response.json()['playlists']['items'][0]
    return {
        "name": playlist['name'],
        "image_url": playlist['images'][0]['url'] if playlist['images'] else None,
        "uri": playlist['uri']
    }

@api.route('/spotify-data/<endpoint>')
def spotify_data(endpoint):
    access_token = get_spotify_access_token(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    if access_token:
        response = fetch_spotify_data(endpoint, access_token)
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({"error": "Failed to fetch data from Spotify"}), response.status_code
    else:
        return jsonify({"error": "Failed to get Spotify access token"}), 500
    
@api.route('/state-toartist/<state>')
def state_toartist_route(state):
    artist_name = get_singer_by_state(state)
    return jsonify({"artist_name": artist_name})