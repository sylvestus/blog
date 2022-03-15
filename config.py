
import os

class Config:
   
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:silvano36@localhost/blog_site'
    #email configurations
    MAIL_SERVER = 'smtp.google.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'silvanussigei19960@gmail.com'
    MAIL_PASSWORD = 'Id34306488'

    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql://snlgmihgbbaxoc:8f2bf7751694bf5022588d039086a0ba4e9fce9559005a4c5c8b8bbec131af5e@ec2-3-209-61-239.compute-1.amazonaws.com:5432/d59v6kg6mo08o9'
   
   
class DevConfig(Config):
     
    
    DEBUG = True

class TestConfig(Config):
    
    DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig  
}
