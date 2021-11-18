from os import uname
from flask import render_template
from flask.wrappers import Request
from . import main
from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from ..models import User
from .forms import UpdateProfile
from .. import db,photos
import requests
from ..utils import Util
from pprint import pprint
import urllib.request,json
from config import Config

@main.route('/',methods=['GET','POST'])

def index():
    '''
    View root page function that returns the index page and its data.
    '''
    title = 'WeatherForecast'


    return render_template('index.html', title = title)



@main.route('/search',methods=['GET','POST'])
def search():
    '''
    View root page function that returns the index page and its data.
    '''
    title = 'WeatherForecast'

    city = "Nairobi"


    base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+Config.API_Key+"&q=" + city

    weather_data = requests.get(base_url).json()
    pprint(Util.parse_weather_data(weather_data))
    data = Util.parse_weather_data(weather_data)

    if request.method == 'POST':

        city = request.form.get("place")

       

        base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+Config.API_Key+"&q=" + city

        weather_data = requests.get(base_url).json()

        pprint(Util.parse_weather_data(weather_data))
        data = Util.parse_weather_data(weather_data)
    return render_template('search.html', title = title, data = data)






@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))





