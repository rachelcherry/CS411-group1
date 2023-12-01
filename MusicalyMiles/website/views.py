from flask import Blueprint, render_template
from flask_login import login_required, current_user
from website.config import SPOTIFY_API_KEY

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user, spotify_api_key=SPOTIFY_API_KEY)