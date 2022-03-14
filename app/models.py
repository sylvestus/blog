from sqlalchemy import desc
from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role = db.Column(db.String(255),index = True)
    bio = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))
    comment = db.relationship('Comments',backref = 'username',passive_deletes=True,lazy='dynamic')
    blog = db.relationship('Blogs', backref='username',passive_deletes=True, lazy='dynamic')
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)

    # @classmethod
    # def get_comments(cls,):

    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.filter_by(comment_id=id).all()
        return comments
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'User {self.username}' 



class Blogs(db.Model):

    __tablename__ = 'blogs_table'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    blog = db.Column(db.String)
    posted_on = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id",ondelete='CASCADE'), nullable=False)
    comments = db.relationship('Comments', backref='title', lazy='dynamic')
    
    

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls):
       
        blogs = Blogs.query.order_by(Blogs.posted_on.desc()).all()
        # blog = Blogs.query.all()
        
        return blogs


    @classmethod
    def deleteBlog(cls, id):
        blog = Blogs.query.get(id)
        db.session.delete(blog)
        db.session.commit()
        return blog
    @classmethod
    def getblogBYid(cls, id):
        blog = Blogs.query.filter_by(id=id).first()
        return blog
    # @classmethod
    # def clear_blogs(cls):
    #     Blogs.all_blogs.clear()
    def __repr__(self):
        return f"Blogs {self.blog}','{self.date}')" 

    


class Comments(db.Model):

    __tablename__ = 'comments'
    id= db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    posted_on = db.Column(db.DateTime,default=datetime.utcnow)
    blogs_id = db.Column(db.Integer, db.ForeignKey("blogs_table.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    def delete_comment(self):
        db.session.remove(self)
        db.session.commit()


    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.filter_by(blogs_id=id).all()
        return comments
def __repr__(self):
        return f"Comments('{self.comment}', '{self.date_posted}')"
    

class Subscriber(db.Model):
    '''
    model class for subscribers
    '''
    __tablename__='subscribers'

    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def getAllMails(cls):
        return Subscriber.query.order_by(Subscriber.id).all()

    def __repr__(self):
        return f'Subscriber {self.username}'

class Quote:
    """
    Class for creating our random quotes.
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote


