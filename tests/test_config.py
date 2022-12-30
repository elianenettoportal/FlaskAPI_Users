""""""

import os 
from config import DevConfig, BaseConfig

""" let check if the config are correct"""
def test_development_config(test_app):
    test_app.config.from_object(DevConfig)
    assert test_app.config["CACHE_TYPE"] == "SimpleCache"
    assert test_app.config["CACHE_DEFAULT_TIMEOUT"] == 10
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == 'sqlite:////mnt/c/Workspace/PowerToFly/FlaskAPI_Users/db/powertofly_test.db'