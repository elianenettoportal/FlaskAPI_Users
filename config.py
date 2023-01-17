"""Flask configuration.
This is a generic Class config for 4 different types of caching
1. (DevConfig) Local caching using flask-caching type SimpleCache
2. (LocalRedisConfig) Local caching to test locally a flask-caching type RedisCache
3. (HerokuRedisConfig) To publish in Heroku, it combines the code in Routers to test SimpleCache with environment variables and External Redis Enterprise Cloud for Caching
4. (DockerConfig) To test flask-caching type RedisCache in a docker using a Docker container. The .env file has the environmental variables

"""
import os

BASE_DIR= os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'base'

class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'dev'
    CACHE_TYPE = "SimpleCache"
    CACHE_DIR= '/tmp'
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+BASE_DIR+'/db/users_test.db'

class LocalRedisConfig(BaseConfig):
    SECRET_KEY = 'dev'
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_HOST= '0.0.0.0'
    CACHE_REDIS_PORT= 6379
    CACHE_DEFAULT_TIMEOUT= 180
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+BASE_DIR+'/db/users.db' 

class HerokuRedisConfig(BaseConfig):
    SECRET_KEY = 'herokuprod'
    CACHE_DEFAULT_TIMEOUT= 180
    CACHE_TYPE = 'SimpleCache'
    CACHE_REDIS_PORT = 6379
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+BASE_DIR+'/db/users.db'

class DockerConfig(BaseConfig):
    SECRET_KEY = 'dockerprod'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+BASE_DIR+'/db/users.db'
    CACHE_TYPE = os.environ['CACHE_TYPE']
    CACHE_REDIS_HOST = os.environ['CACHE_REDIS_HOST']
    CACHE_REDIS_PORT = os.environ['CACHE_REDIS_PORT']
    CACHE_REDIS_DB = os.environ['CACHE_REDIS_DB']
    CACHE_REDIS_URL = os.environ['CACHE_REDIS_URL']
    CACHE_DEFAULT_TIMEOUT = os.environ['CACHE_DEFAULT_TIMEOUT']
   
