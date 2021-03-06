import os
import re


class Config:
    """
    General configuration parent class
    """

    SECRET_KEY = os.environ.get("SECRET_KEY")
    QUOTE_API_BASE_URL = "http://quotes.stormconsultancy.co.uk/random.json"
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    #  email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    DEBUG = True


class ProdConfig(Config):
    """
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """

    uri = os.getenv("DATABASE_URL")  # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = uri
    


class DevConfig(Config):
    """
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """

    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://obafemi:Bentamjay1@localhost/blogapp"
    )
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://obafemi:Bentamjay1@localhost/blogapp_test'
    


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig,
}
