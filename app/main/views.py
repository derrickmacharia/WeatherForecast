from os import uname
from flask import render_template
from . import main
from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from ..models import User
from .forms import UpdateProfile
from .. import db,photos
# from ..request import get_weather


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    title = 'WeatherForecast'
    return render_template('index.html', title = title)

    
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
# @main.route('/weather/review/new/<int:id>', methods = ['GET','POST'])
# def new_review(id):
#     form = ReviewForm()
#     weather = get_weather(id)

#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data
#         new_review = Review(weather.id,title,review)
#         new_review.save_review()
#         return redirect(url_for('weather',id = weather.id))

#     title = f'{weather.title} review'
#     return render_template('new_review.html',title = title ,review_form = form,weather = weather)

# @main.route('/weather/<int:id>')
# def weather(id):
#     '''
#     View weather page function that returns the weather details page and its data
#     '''
#     weather = get_weather()
#     title = f'{weather.title}'
#     reviews = Review.get_reviews(weather.id)

#     return render_template('weather.html',)
    
