# import os.path


DEBUG = True

# basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') 
SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///app.db' 
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'senha-para-usar-o-form'