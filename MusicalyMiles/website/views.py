import datetime
from flask import Blueprint, render_template, Flask, request, session, redirect, jsonify, current_app
from flask_login import login_required, current_user
from .config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, GOOGLE_CLIENT_KEY, OPEN_WEATHER_KEY
from .singers import get_playlist_by_temperature
import requests

import base64
import hashlib
import os

def generate_code_verifier():
    return base64.urlsafe_b64encode(os.urandom(40)).decode('utf-8').rstrip('=')

def generate_code_challenge(verifier):
    sha256 = hashlib.sha256(verifier.encode('utf-8')).digest()
    return base64.urlsafe_b64encode(sha256).decode('utf-8').rstrip('=')

def refresh_access_token(refresh_token):
    response = requests.post(
        'https://accounts.spotify.com/api/token',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': SPOTIFY_CLIENT_ID,
        }
    )
    if response.status_code == 200:
        current_app.logger.debug(f"token refreshed")
        return response.json().get('access_token')
    else:
        current_app.logger.error(f"Failed to refresh token: {response.status_code}, Response: {response.text}")
        return None

def store_access_token(response_json):
    access_token = response_json.get('access_token')
    refresh_token = response_json.get('refresh_token')
    expires_in = response_json.get('expires_in')  # Time in seconds until the token expires

    # Calculate the expiry time as a timestamp
    expiry_time = datetime.datetime.now() + datetime.timedelta(expires_in)

    # Store the access token and expiry time in the session or a secure place
    session['access_token'] = access_token
    session['refresh_token'] = refresh_token
    session['expiry_time'] = expiry_time.timestamp()
    
def token_is_expired():
    expiry_time = session.get('expiry_time')
    if not expiry_time:
        return True  # Assume expired if no expiry time is stored

    # Compare current time with the expiry time
    return datetime.datetime.now() >= datetime.datetime.fromtimestamp(expiry_time)


views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("index.html", user=current_user, spotify_api_key=SPOTIFY_CLIENT_ID, google_api_key=GOOGLE_CLIENT_KEY, open_weather_key=OPEN_WEATHER_KEY)

@views.route('/login')
def login():
    return render_template('login.html', SPOTIFY_CLIENT_ID=SPOTIFY_CLIENT_ID)

@views.route('/start_oauth')
def start_oauth():
    verifier = generate_code_verifier()
    challenge = generate_code_challenge(verifier)
    session['verifier'] = verifier  # Store verifier in session

    params = {
        'client_id': SPOTIFY_CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': 'http://127.0.0.1:5000/callback',
        'scope': 'playlist-modify-private',
        'code_challenge_method': 'S256',
        'code_challenge': challenge
    }
    query_string = '&'.join([f'{key}={value}' for key, value in params.items()])
    auth_url = f'https://accounts.spotify.com/authorize?{query_string}'
    return redirect(auth_url)

@views.route('/callback')
def callback():
    code = request.args.get('code')
    verifier = session.pop('verifier', None)

    if not verifier:
        return render_template('login.html', SPOTIFY_CLIENT_ID=SPOTIFY_CLIENT_ID)

    # Exchange the code for an access token
    response = requests.post(
        'https://accounts.spotify.com/api/token',
        data={
            'client_id': SPOTIFY_CLIENT_ID,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://127.0.0.1:5000/callback',
            'code_verifier': verifier
        }
    )
    response_json = response.json()
    store_access_token(response_json)
    
    access_token = session.get('access_token')
    
    current_app.logger.debug(f"Access Token: {session.get('access_token')}")
    current_app.logger.debug(f"Token Exchange Response: {response.json()}")

    # Fetch Spotify profile information
    headers = {'Authorization': f'Bearer {access_token}'}
    profile_response = requests.get('https://api.spotify.com/v1/me', headers=headers)
    current_app.logger.debug(f"profile_response: {profile_response}")
    if profile_response.status_code != 200:
        current_app.logger.error(f"Failed to fetch Spotify profile: {profile_response.status_code}, Response: {profile_response.text}")
    else:
        profile_info = profile_response.json()
        current_app.logger.debug(f"Spotify Profile Info: {profile_info}")

    # Redirect the user to the index page
    return render_template("index.html", user=current_user, spotify_api_key=SPOTIFY_CLIENT_ID, google_api_key=GOOGLE_CLIENT_KEY, open_weather_key=OPEN_WEATHER_KEY)

@views.route('/process_temp', methods=['POST'])
def process_temp():
    current_app.logger.debug("Received AJAX request")
    data = request.json
    temp = data['temp']
    current_app.logger.debug(f"Temp received: {temp}")
    
    # Use singers.py to convert the temp to Spotify ID
    spotify_id = get_playlist_by_temperature(temp)
    
    # You can then do further processing or return the Spotify ID
    return jsonify({'spotify_id': spotify_id})

@views.route('/playlist', methods=['GET'])
def playlist():
    temp = request.args.get('temp')

    if not temp:
        return "temp not provided", 400

    spotify_id = get_playlist_by_temperature(temp)
    current_app.logger.debug(f"spotify_id received: {spotify_id}")

    # Retrieve the access token from the session or another secure storage
    access_token = session.get('access_token')
    current_app.logger.debug(f"Access Token: {access_token}")
    
    refresh_token = session.get('refresh_token')
    current_app.logger.debug(f"Refresh Token: {refresh_token}")

    if not access_token or token_is_expired():
        access_token = refresh_access_token(refresh_token)
        if not access_token:
            return jsonify({'status': 'error', 'message': 'Failed to refresh access token'}), 401
        session['access_token'] = access_token  # Update the session with the new access token
        store_access_token({'access_token': access_token, 'expires_in': 3600})  # Assuming 1 hour expiry for new token

    # Make a GET request to the Spotify API to fetch the playlist
    headers = {'Authorization': f'Bearer {access_token}'}
    playlist_response = requests.get(f'https://api.spotify.com/v1/playlists/{spotify_id}', headers=headers)

    if playlist_response.status_code != 200:
        current_app.logger.error(f"Failed to fetch playlist: {playlist_response.status_code}, Response: {playlist_response.text}")
        return jsonify({'status': 'error', 'message': 'Failed to fetch playlist'}), 500

    playlist_data = playlist_response.json()

    return render_template('playlist.html', temp=temp, playlist=playlist_data)

@views.route('/save_playlist', methods=['POST'])
def save_playlist():
    # Retrieve the access token from the session or another storage
    access_token = session.get('access_token')
    refresh_token = session.get('refresh_token')
    if not access_token or token_is_expired():
        access_token = refresh_access_token(refresh_token)
        if not access_token:
            return jsonify({'status': 'error', 'message': 'Failed to refresh access token'}), 401
        session['access_token'] = access_token  # Update the session with the new access token
        store_access_token({'access_token': access_token, 'expires_in': 3600})  # Assuming 1 hour expiry for new token

    # Get data from the request
    data = request.json
    playlist_id = data.get('playlistId')
    
    if not playlist_id:
        return jsonify({'status': 'error', 'message': 'Playlist ID is missing'}), 400
    
    current_app.logger.debug(f"playlistId: {playlist_id}")

    headers = {'Authorization': f'Bearer {access_token}'}
    playlist_details_response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}', headers=headers)

    if playlist_details_response.status_code != 200:
        return jsonify({'status': 'error', 'message': 'Failed to fetch playlist details'}), 500

    playlist_details = playlist_details_response.json()
    original_playlist_name = playlist_details.get('name')
    
    playlist_tracks_response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers=headers)

    if playlist_tracks_response.status_code != 200:
        return jsonify({'status': 'error', 'message': 'Failed to fetch tracks from the playlist'}), 500

    tracks_data = playlist_tracks_response.json()
    track_uris = [track['track']['uri'] for track in tracks_data['items'] if track['track']]

    # Create a new playlist
    headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
    user_profile = requests.get('https://api.spotify.com/v1/me', headers=headers).json()
    user_id = user_profile.get('id')

    create_playlist_response = requests.post(
        f'https://api.spotify.com/v1/users/{user_id}/playlists',
        headers=headers,
        json={'name': original_playlist_name, 'public': False}  # Set to True if you want the playlist to be public
    )

    if create_playlist_response.status_code != 201:
        return jsonify({'status': 'error', 'message': 'Failed to create playlist'}), 500

    # Add tracks to the playlist if any
    playlist_id = create_playlist_response.json().get('id')
    if track_uris:
        add_tracks_response = requests.post(
            f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks',
            headers=headers,
            json={'uris': track_uris}
        )
        if add_tracks_response.status_code != 201:
            return jsonify({'status': 'error', 'message': 'Failed to add tracks to the playlist'}), 500

    return jsonify({'status': 'success', 'playlist_id': playlist_id})


