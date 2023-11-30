from flask import Flask, redirect, request, session
import google.auth
from google.oauth2.credentials import Credentials

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Google Cloud API credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'YOUR_REDIRECT_URI'
scope = ['https://www.googleapis.com/auth/maps']

# Google OAuth endpoints
authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
token_url = 'https://accounts.google.com/o/oauth2/token'

@app.route('/')
def index():
    authorization_url, state = google.auth.default(
        client_id=client_id, client_secret=client_secret, scope=scope,
        redirect_uri=redirect_uri
    )

    session['oauth_state'] = state
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    token = google.auth.transport.requests.Request().from_request(
        request.url, redirect_uri=redirect_uri, state=session['oauth_state']
    )

    credentials = Credentials.from_authorized_user_info(
        token, client_id=client_id, client_secret=client_secret
    )

    # Use 'credentials' to make authorized API requests

    return 'Authenticated successfully!'

if __name__ == '__main__':
    app.run(debug=True)
