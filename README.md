
<h2> Description</h2>
This is an API in Python to fetch more than 1MM records.It contains Searching and the Pagination.
For this implementation I am using Flask Framerok with SQLite database, cache-control, and dockerization

<h1> FlaskAPI Users </h1>

---------------------------------------------------------------------------------------------------------------------------------------------------
:fire:<mark>NEW VERSION</mark><br>
> &nbsp;&nbsp;I made a few changes to the project after had it been delivered. This remains original, I created a new Repository if you  would like to consider.<br>
[-> here](https://github.com/elianenettoportal/FlaskAPI_Users_2)
1. Fixed gitignore
2. Improved RedisCache in localhost and Docker
3. Clean code and comments
---------------------------------------------------------------------------------------------------------------------------------------------------

<h2> Description</h2>
This is an API in Python to fetch more than 1MM records.It contains Searching and the Pagination.
For this implementation I am using Flask Framerok with SQLite database, cache-control, and dockerization

<h2>Project Details</h2>

Flask Framework is a Python microframework for web development. It means that Flask uses python as the main language for the server-side implementation and also javascript, HTML, and CSS to build the client-side templates  It is a powerful tool, and comes with Werkzeg WSGI and Jinja2 libraries.
</br>
</br>

### Package structure
>root<br>
&nbsp;&nbsp;&nbsp;&nbsp;-db<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-production database(1MM registers)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-test database(5 registers)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-user_list.py(file to test and create sqlite database)<br>
&nbsp;&nbsp;&nbsp;&nbsp;-main <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-model<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-user(user schema definition)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-static(static files, image and css)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-templates<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-index.html(landing page template)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-users<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-blueprint.py( file to manipulate users routers)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-templates (users.html - users page with pagination, users table result)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-__init__.py( instanciate the Flask app and app configurations)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-routerss.py( landing page router )<br> 
&nbsp;&nbsp;&nbsp;&nbsp;-tests<br>
&nbsp;&nbsp;&nbsp;&nbsp;-app.py              ( this file is the application entry point.)<br>
&nbsp;&nbsp;&nbsp;&nbsp;-config.py           ( the Flask app configurations for Dev and Production)<br>
&nbsp;&nbsp;&nbsp;&nbsp;-.env                ( environment variables to redis)<br>
&nbsp;&nbsp;&nbsp;&nbsp;-docker-compile      ( script to generate the containers Flask and Redis AND run Dockerfile)<br>
&nbsp;&nbsp;&nbsp;&nbsp;-Dockerfile          ( the docker commands to build a container for python env)<br>
&nbsp;&nbsp;&nbsp;&nbsp;-Procfile            ( the commands to publish Heroku)<br>
&nbsp;&nbsp;&nbsp;&nbsp;-requirements.txt    ( the libraries for production)<br>
&nbsp;&nbsp;&nbsp;&nbsp;-requirements-dev.txt( the libraries for test environment)<br>

* Python Language:<br>
 It is perfect for POCs and small-time developments. The leaders for python FE are Django and Flask.

* WSGI:<br>
It is a web server gateway interface for python, a universal interface, a specification between the web server and web app.

* Welzeug:<br>
 Tool kit WSGI to implement functions, for instance, requests.

* Jinja2:<br>
 It is a web template to render web pages. It accepts python variables in the HTML as well as python loops and conditionals.

* Cache-Control:<br>
 It is a process in that web browsers save website resources in order to load them faster next time.
 It is in HTTP headers, used to specify browser caching policies in both client requests and server responses. These policies include how a resource is cached, where  it is cached and the maximum age before expiring.<br>
 *For this development, we will be using Flask-Caching and RedisCache.*

* ORM:<br>
 **Object Relational Mapping** is a technique to write schemas of datatables. SQLAlchemy is an ORM for python and the 
 Flask-SQLAlchemy is an extension for Flask that supports SQLAlchemy. Since I am new to python developments it is recommended due to its facility of using.

* Caching Redis:<br>
 It is a Client Side caching technique for high-performance services. It is a Key-Value pair database. We can use to store data used all the time, data that doesn´t change much and/or long or slow query results.</p>

* Heroku:<br>
 It is a **Cloud Platform as a Service**, PaaS. Until 2 months ago Heroku had free dynos available, however, since then, it is necessary to pay $5 dollars/mo.

* Virtual Environment<br>
 When developing in python we need to create a virtual environment to pip/install the packages and run the tool. A library creates an env on top of an existing Python  installation.

* Rquirements txt:<br>
 It is like a NPM for Node jS applications, in this file we keep the libraries installed and, later on, it becomes a reference to Heroku or Docker to install and run the application.

tools:
> 1) Vscode in windows
> 2) `WSL2` the windows Subsystem for Linux:
>    Since most of libraries for python are linux based, it is recommended to install WSL2 a linux distributton pip python for development purpose.
> 3) Linux Distribution (lateste)
>   Choose the latest version of Linux for windows
> 4) `Docker Desktop`
>    I downloaded a SQLiteBrowser docker t manipulate data for SQLite database 
> 5) `Git`
>    For version control 
> 6) `Heroku`
>    Used Heroku to publish the API 
> 7) `VSCode`
> 8) `Docker for sqlite`

packages:
> python3 -> It is the Python Language Interpreter <br>
> sqlite3 -> A module to integrate the SQLite with Python <br>
> Flask   -> SQLAlchemy -> Extension for Flask that supports SQLAlchemy the ORM of Python <br>
> redis   -> Client side caching control <br>
> gunicorn-> Python WSGI HTTP Server for Unix. The green unicorn light server<br>
> Flask Caching -> Extension for Flask that supports Cache Cotntrol<br>
> Redis Server -> To run RedisCache localhost.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Building process:<br>
**Heroku Publish**:<br>
> The building process in Heroku uses the Procfile that specifies the commands to execute by Heroku app on startup. Quite simply, it only needs to know what is the main file entry point of the application and the Server to run, in this case it is gunicorn.<br>
> In Heroku webpage, I integrated Github into the deploy method and configured the buildpack script with the WSGI gunicorn. Heroku gets the latest version os the tool from the main branch and performs the publish.

**Docker Publish:**<br> 
**Start the Redis instance with Docker**<br>
> Dockerization <br>
I created a docker file to install python, install requirements.tx and build the container.<br>
I created a docker compose to build the docker containers Fask Api + Redis cache control.<br>
To compile, clone this project, go inside the root package and run :<br>
`run docker-compose up -d --build` <br> 
