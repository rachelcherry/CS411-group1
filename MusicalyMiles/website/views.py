from flask import Blueprint, render_template, Flask, request, session, redirect, jsonify, current_app
from flask_login import login_required, current_user
from .config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, GOOGLE_CLIENT_KEY, OPEN_WEATHER_KEY
from .singers import get_singer_by_state
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("index.html", user=current_user, spotify_api_key=SPOTIFY_CLIENT_ID, google_api_key=GOOGLE_CLIENT_KEY, open_weather_key=OPEN_WEATHER_KEY)

@views.route('/login')
def login():
    return render_template('login.html', SPOTIFY_CLIENT_ID=SPOTIFY_CLIENT_ID)

@views.route('/callback')
def callback():
    code = request.args.get('code')
    # Exchange the code for an access token
    response = requests.post(
        'https://accounts.spotify.com/api/token',
        data={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://127.0.0.1:5000/callback',
            'client_id': 'SPOTIFY_CLIENT_ID',
            'client_secret': 'SPOTIFY_CLIENT_SECRET'
        }
    )
    response_json = response.json()
    access_token = response_json.get('access_token')
    # Save the access token in the session
    session['access_token'] = access_token
    # Redirect the user to the index page
    return render_template("index.html", user=current_user, spotify_api_key=SPOTIFY_CLIENT_ID, google_api_key=GOOGLE_CLIENT_KEY, access_token=access_token)

@views.route('/process_state', methods=['POST'])
def process_state():
    current_app.logger.debug("Received AJAX request")
    data = request.json
    state = data['state']
    current_app.logger.debug(f"State received: {state}")
    data = request.json
    state = data['state']
    
    # Use singers.py to convert the state to Spotify ID
    spotify_id = get_singer_by_state(state)
    
    # You can then do further processing or return the Spotify ID
    return jsonify({'spotify_id': spotify_id})

@views.route('/playlist', methods=['GET', 'POST'])
def playlist():
    # Check if the request has JSON data
    if request.method == 'POST':
        data = request.get_json()
        state = data.get('state')
    elif request.method == 'GET':
        state = request.args.get('state')

    if not state:
        return "State not provided", 400

    spotify_id = get_singer_by_state(state)
    current_app.logger.debug(f"spotify_id received: {spotify_id}")
    client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    playlist = sp.playlist(spotify_id)

    return render_template('playlist.html', state=state, playlist=playlist)
