from flask import Blueprint, render_template, request, redirect
from main.model import user
from main import db
from main import cache
import time

# instanciate objects
users = Blueprint('users', __name__, template_folder='templates')
User = user.User;

"""
    These endpoints are used in the User Router to fetch users.
    They are cached and the response is stored based on Query String. 
    The timeout is default, set in the config app - 300 seconds
    timeout param is the time that this response will be cached in Redis memory.
    
    NOTE: RedisCache is already available in werkzeug >= 0.7 no need for a special configuration
"""

# Main router not cached, used when back from Edit or Delete
# localhost:5000/users/
@users.route('/')
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


# Main router  cached, used in Button All Results
# localhost:5000/users/memoize
@users.route('/memoize')
@cache.memoize()
def users_list_memo():
    start_time = time.time()
    args       = request.args
    per_page   = 15
    page_num   = args.get('page_num') if args.get('page_num') != None else 1
    try:
        users = User.query.order_by(User.lastName).paginate(page=int(page_num), per_page=int(per_page), error_out=True)
    except Exception as err:
        print("ERROR** Module User Router - users_list()", str(err))
        users = []; filterName='';

    print("--- %s memoize ---" % (time.time() - start_time))       
    return render_template('users/users.html', data_set=users)

"""
param query_string: 
    When True, the cache key used will be the result of hashing the ordered query string parameters. 
    This avoids creating different caches for the same query just because the parameters were passed in a different order.
"""
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

''' 
    By default, Flask accepts GET requests for all routes, I added here it to allow GET and POST requests
    if request.form checks if someone just submitted the form. 
    If they did, we can access the data that they submitted through the request.form variable
    Flask represents all of the form data as an ImmutableMultiDict, which is just a fancy Python dictionary.
    It stored our user's input as a tuple
'''
# localhost:5000/users/create
@users.route('/create',methods=["GET", "POST"])
def user_create():
    if request.form:
        newUser = User(firstName=request.form.get("firstName"), lastName=request.form.get("lastName"), bio=request.form.get("bio"))
        db.session.add(newUser)
        db.session.commit()
    return render_template('users/user_create.html')

'''
    This method will just redirect to a delete or update template
'''
# localhost:5000/users/redirect
@users.route("/redirect")
def user_redirect():
    try:
        args = request.args
        if args.get('selected'):
            userFound = User.query.filter_by(id=args.get('selected')).first()
        if args.get('action') == 'edit' and userFound:
            return render_template('users/user_update.html', selected=userFound)
        elif args.get('action') == 'delete' and userFound:
            return render_template('users/user_delete.html', selected=userFound)
        else:
            return redirect("/users/")
    except Exception as err:
        print("ERROR** Module User Router - redirect()", str(err))
        return redirect("/users/")

'''
    Find user by the id selected and sent by param and edit the first name
'''
# localhost:5000/users/update
@users.route("/update", methods=["POST"])
def user_update():
    try:
        firstName = request.form.get("firstName")
        userId    = request.form.get("userId")
        userFound = User.query.filter_by(id=userId).first()
        userFound.firstName = firstName
        db.session.commit()
    except Exception as err:
        print("ERROR** Module User Router - redirect()", str(err))
    return redirect("/users/")


'''
    Find user by the id selected and sent by param and delete it by id
'''
# localhost:5000/users/delete
@users.route("/delete", methods=["POST"])
def user_delete():
    try:
        userId = request.form.get("userId")
        userFound = User.query.filter_by(id=userId).first()
        db.session.delete(userFound)
        db.session.commit()
    except Exception as err:
        print("ERROR** Module User Router - redirect()", str(err))
    return redirect("/users/")