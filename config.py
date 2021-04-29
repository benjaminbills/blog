import os
import re


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get("SECRET_KEY")


class ProdConfig(Config):
    """
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    pass


class DevConfig(Config):
    """
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://obafemi:Bentamjay1@localhost/blogapp'

    DEBUG = True


class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://obafemi:Bentamjay1@localhost/login_test'
    pass


config_options = {"development": DevConfig,
                  "production": ProdConfig, 'test': TestConfig}
