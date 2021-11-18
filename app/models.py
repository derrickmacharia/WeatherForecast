from . import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    # relationships
    
   

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

# class Review:

#     all_reviews = []

#     def __init__(self,weather_id,title,review):
#         self.weather_id = weather_id
#         self.title = title
#         self.review = review


#     def save_review(self):
#         Review.all_reviews.append(self)


#     @classmethod
#     def clear_reviews(cls):
#         Review.all_reviews.clear()
#     @classmethod
#     def get_reviews(cls,id):
#         response = []

#         for review in cls.all_reviews:
#             if review.weather_id == id:
#                 response.append(review)

#         return response