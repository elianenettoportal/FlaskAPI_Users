# this file can have all independente routers and open routers-those that don´t need authentication
from main import app
from flask import render_template
from main import cache
from random import randint
import redis
import os

# External Redis Enterprise Cloud - Caching
PASSWORD = os.environ.get('REDISCLOUD_PASS', None)
URI      = os.environ.get('REDISCLOUD_URI', None)
PORT     = os.environ.get('REDISCLOUD_PORT', None)
if PASSWORD == None:
    dbRedis=redis.from_url('redis://default:FAKE@TEST')
else:
    dbRedis=redis.from_url('redis://default:'+PASSWORD+'@'+URI+':'+PORT)


# Landing page router
@app.route("/")
@cache.cached(query_string=True)
def index():
    return render_template('index.html')

# (TEST) I leep this endpoint to test my caching
#/users/test-cache
@app.route('/test-cache')
@cache.cached(timeout=30, query_string=True)
def test_cache():
    randnum = randint(1,1000)
    return f'<h1>The number is : {randnum}</h1><br><h3>It must chamge after 30 seconds Local 3 min in Docker<h3>'

# (TEST) RedisCache available in werkzeug >= 0.7
#/users/test-redis
@app.route('/test-redis')
@cache.memoize(timeout=15)
def test_redis():
    randnum = randint(1,1000)
    return f'<h1>The number is : {randnum}</h1><br><h3>It must chamge after 15 seconds Local 180 seconds(1min) in Docker<h3>'

# (TEST) Redis Enterprise Cloud caching - get last name added from cache
#/users/test-redis-cache
@app.route('/test-redis-cache')
def test_rediscache():
    name    = dbRedis.get('name')
    if name:
        return f'<h1>Found : {name}</h1>'
    else:
        return f'<h1>Found : {name}</h1>'

# (TEST) External Redis Enterprise Cloud caching - save a name
#/users/test-redis-cache/eliane
@app.route('/test-redis-cache/<name>')
def test_save_rediscache(name):
    dbRedis.set('name',name)
    return 'Name updated.'