"""Flask configuration."""
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
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+BASE_DIR+'/db/powertofly_test.db'

class LocalRedisConfig(BaseConfig):
    SECRET_KEY = 'dev'
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_HOST= '0.0.0.0'
    CACHE_REDIS_PORT= 6379
    CACHE_DEFAULT_TIMEOUT= 180
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+BASE_DIR+'/db/powertofly.db' 

class HerokuRedisConfig(BaseConfig):
    SECRET_KEY = 'herokuprod'
    CACHE_DEFAULT_TIMEOUT= 180
    CACHE_TYPE = 'SimpleCache'
    CACHE_REDIS_PORT = 6379
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+BASE_DIR+'/db/powertofly.db'

class DockerConfig(BaseConfig):
    SECRET_KEY = 'dockerprod'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+BASE_DIR+'/db/powertofly.db'
    CACHE_TYPE = os.environ['CACHE_TYPE']
    CACHE_REDIS_HOST = os.environ['CACHE_REDIS_HOST']
    CACHE_REDIS_PORT = os.environ['CACHE_REDIS_PORT']
    CACHE_REDIS_DB = os.environ['CACHE_REDIS_DB']
    CACHE_REDIS_URL = os.environ['CACHE_REDIS_URL']
    CACHE_DEFAULT_TIMEOUT = os.environ['CACHE_DEFAULT_TIMEOUT']
   
