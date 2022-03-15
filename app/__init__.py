from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_simplemde import SimpleMDE
import os


login_manager = LoginManager()
login_manager.session_protection= 'strong'
login_manager.login_view='auth.login'

bootstrap=Bootstrap()
db = SQLAlchemy()
mail= Mail()
simple = SimpleMDE()

def create_app(config_name):
    app = Flask(__name__)
    

     # Creating the app configurations
    # app.config.from_object(config_options[config_name])
    # app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://moringa:silvano36@localhost/blog_site'
    
     

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.ge("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False



    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
   
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

    #Registering the blueprint
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint,url_prefix = '/')
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')


    return app