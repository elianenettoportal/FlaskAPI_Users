from flask import Flask
from flask_sqlalchemy import SQLAlchemy # this is the import for the ORM 
from flask_caching import Cache # this is the Import Cache from flask_caching module

# take environment variables from .env
from dotenv import load_dotenv 
if(load_dotenv() == False): 
    raise RuntimeError('ERROR - Env variables not loaded')
from config import DevConfig, HerokuRedisConfig, DockerConfig,LocalRedisConfig

# instanciate the Cache class
cache = Cache()

#instanciate Flask
app = Flask(__name__)

# NOTE: The secret key is used to cryptographically-sign the cookies used for storing the session identifier.
app.secret_key = "testpowertofly_BRAZIL"

"""
This app is configured to run 3 different types of caching. 
1. Caching with Redis in a Docker container
2. Flask-Caching type RedisCache
3. External Redis Enterprise Cloud Caching published in Heroku
"""
#app.config.from_object(DevConfig)
#(Uncomment below to run the Docker Redis config)
app.config.from_object(DockerConfig)

#(Uncomment bellow for local dev or redis cache)
#  remember to start client redis
#       >> sudo service redis-server start
#       >> redis-cli 
#app.config.from_object(LocalRedisConfig)

#(Uncomment below to run HEROKU config)
#app.config.from_object(HerokuRedisConfig)

# add app to the objects  
cache = Cache(app)
db    = SQLAlchemy(app)

