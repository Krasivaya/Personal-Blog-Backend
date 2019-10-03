import os


class Config:
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

class ProdConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SECRET_KEY="testkeyindevconfig"
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://wecode:wecode@localhost/blog"
    DEBUG = True

class TestConfig(Config):
    SECRET_KEY="testkeyintestconfig"
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://wecode:wecode@localhost/blog_test"

configurations = {
    "production":ProdConfig,
    "development":DevConfig,
    "testing":TestConfig
} 