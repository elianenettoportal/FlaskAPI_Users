### this file is the application entry point. 
from main import app
from main.users.blueprint import users

# import routers to main file
from main import routers

# register the blueprints of the API
# localhost:5000/users
app.register_blueprint(users, url_prefix='/users')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

