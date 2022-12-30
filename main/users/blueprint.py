from flask import Blueprint, render_template, request
from main.model import user
from main import cache
import time

# instanciate objects
users = Blueprint('users', __name__, template_folder='templates')
User = user.User;

"""
    When True, the cache key used will be the result of hashing the ordered query string parameters. 
    This avoids creating different caches for the same query just because the parameters were passed in a different order.
    (CACHED) These two endpoints are User Router to fetch users.
    They are cached and the response stored based on Query String. 
    The timeout is default, set in the config app - 300 seconds
    timeout which is the time that this response will be cached in Redis memory.
    
    NOTE: RedisCache is already available in werkzeug >= 0.7 no need for a special configuration
"""
# localhost:5000/users/
@users.route('/')
@cache.memoize()
def users_list():
    start_time = time.time()
    args       = request.args
    per_page   = 15
    page_num   = args.get('page_num') if args.get('page_num') != None else 1
    try:
        users = User.query.order_by(User.lastName).paginate(page=int(page_num), per_page=int(per_page), error_out=True)
    except Exception as err:
        print("ERROR** Module User Router - users_list()", str(err))
        users = []; filterName='';

    print("--- %s seconds ---" % (time.time() - start_time))       
    return render_template('users/users.html', data_set=users)


# localhost:5000/users/search
@users.route('/search')
@cache.cached(query_string=True)
def users_search():
    start_time = time.time()
    args       = request.args
    per_page   = 15
    filterName = args.get("name")
    page_num   = args.get('page_num') if args.get('page_num') != None else 1
    try:
        if filterName != None and filterName != '':
            filterCondition = (User.firstName.ilike("%"+str(filterName)+"%") | User.lastName.ilike("%"+str(filterName)+"%"))
            users = User.query.filter(filterCondition).order_by(User.lastName).paginate(page=int(page_num), per_page=int(per_page), error_out=True)
        else:
            users = User.query.order_by(User.lastName).paginate(page=int(page_num), per_page=int(per_page), error_out=True)
    except Exception as err:
        print("ERROR** Module User Router - users_search()", str(err))
        users = []; filterName='';

    print("--- %s seconds ---" % (time.time() - start_time)) 
    return render_template('users/users.html', filterName=filterName, data_set=users)

