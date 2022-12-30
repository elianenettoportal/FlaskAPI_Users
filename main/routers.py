# this file can have all independente routers and open routers-those that don´t need authentication
from main import app
from flask import render_template
from main import cache
from random import randint
import redis
import os

# Landing page router
@app.route("/")
@cache.cached(query_string=True)
def index():
    return render_template('index.html')

"""
Test cache endpoint is a function to comfirm that flask-caching is working. It will generate a random number only after 30s.
The function is decorated with flask-caching params:
                timeout - the waiting time to renew the cache
                query_string - Default False. When True, the cache key
                     used will be the result of hashing the
                     ordered query string parameters. This
                     avoids creating different caches for
                     the same query just because the parameters
                     were passed in a different order
"""

# (TEST) I leep this endpoint to test my caching
#/users/test-cache
@app.route('/test-cache')
@cache.cached(timeout=30, query_string=True)
def test_cache():
    randnum = randint(1,1000)
    return f'<h1>The number is : {randnum}</h1><br><h3>It must chamge after 30 seconds Local 3 min in Docker<h3>'


"""
The theory behind memoization is that if you have a function you need to call several times in one request, 
it would only be calculated the first time that function is called with those arguments. 
For example, an sqlalchemy object that determines if a user has a role. 
You might need to call this function many times during a single request
"""

# (TEST) RedisCache available in werkzeug >= 0.7
#/users/test-redis
@app.route('/test-redis')
@cache.memoize(timeout=15)
def test_redis():
    randnum = randint(1,1000)
    return f'<h1>The number is : {randnum}</h1><br><h3>It must chamge after 15 seconds Local 180 seconds(1min) in Docker<h3>'

"""
In the below code we can access the External Redis Enterprise Cloud for Caching. The environment variables are set in Heroku var settings

First, we need to create the Redis Enterprise cloud subscription and database, luckily they have a Free AWS cloud with 30MB RAM to start.
Secondly, we need to copy the public endpoint and password. Save these in Heroku Settings - var settings
when the tool runs it fills up the below variables and we are able to test the database.

This is a simple test, it creates a name and searches if it exists. The first endpoint saves the name and the second gives you back if it is saved correctely
1. <url>/test-redis-cache/NAMEYOUWANT
2. <url>/test-redis-cache 
"""

# External Redis Enterprise Cloud - Caching
PASSWORD = os.environ.get('REDISCLOUD_PASS', None)
URI      = os.environ.get('REDISCLOUD_URI', None)
PORT     = os.environ.get('REDISCLOUD_PORT', None)
if PASSWORD == None:
    dbRedis=redis.from_url('redis://default:FAKE@TEST')
else:
    dbRedis=redis.from_url('redis://default:'+PASSWORD+'@'+URI+':'+PORT)

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