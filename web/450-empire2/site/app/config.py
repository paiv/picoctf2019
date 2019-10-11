import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
 SECRET_KEY = 'picoCTF{your_flag_is_in_another_castle12345678}'
 SQLALCHEMY_DATABASE_URI = 'sqlite://'
 #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABSE_URL') or 'sqlite:///'+os.path.join(basedir,'app.db')
 SQLALCHEMY_TRACK_MODIFICATIONS = False
