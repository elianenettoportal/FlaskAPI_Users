from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
# take environment variables from .env.)
if(load_dotenv() == False): 
    raise RuntimeError('ERROR - Env variables not loaded')

from config import DevConfig, HerokuRedisConfig, DockerConfig,LocalRedisConfig

# For redis caching database
import os
import redis

# this is the Import Cache from flask_caching module
from flask_caching import Cache

# instanciate the Cache class
cache = Cache()

#instanciate Flask
app = Flask(__name__)

# The secret key is used to cryptographically-sign the cookies used for storing the session identifier.
app.secret_key = "testpowertofly_BRAZIL"

# Docker Redis config
#app.config.from_object(DockerConfig)
# NOTE: Uncomment bellow for local dev or redis cache
#  remember to start client redis
#       >> sudo service redis-server start
#       >> redis-cli 
#app.config.from_object(LocalRedisConfig)
app.config.from_object(HerokuRedisConfig)

# add app to the objects  
cache = Cache(app)
db    = SQLAlchemy(app)

