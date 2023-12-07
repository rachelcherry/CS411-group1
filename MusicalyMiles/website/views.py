from flask import Blueprint, render_template, Flask
from flask_login import login_required, current_user
from .config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("index.html", user=current_user, spotify_api_key=SPOTIFY_CLIENT_ID)

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
    return redirect('/')