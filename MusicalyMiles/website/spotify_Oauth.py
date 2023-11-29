from flask import Flask, redirect, request, session
import requests
import base64
import os

app = Flask(__name__)

# Spotify API credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'YOUR_REDIRECT_URI'
scope = 'user-read-private user-read-email'  # Add required scopes

# Spotify API endpoints
authorize_url = 'https://accounts.spotify.com/authorize'
token_url = 'https://accounts.spotify.com/api/token'
profile_url = 'https://api.spotify.com/v1/me'

@app.route('/')
def index():
    # Redirect to Spotify authorization URL
    auth_url = f"{authorize_url}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=code"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Handle callback from Spotify
    code = request.args.get('code')
    token_data = get_access_token(code)
    user_data = get_user_data(token_data['access_token'])
    return f"Hello, {user_data['display_name']}!"

def get_access_token(code):
    # Request access token from Spotify
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode('utf-8')).decode('utf-8')
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
    }
    headers = {
        'Authorization': f'Basic {auth_header}',
    }
    response = requests.post(token_url, data=data, headers=headers)
    return response.json()

def get_user_data(access_token):
    # Get user data from Spotify
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.get(profile_url, headers=headers)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
