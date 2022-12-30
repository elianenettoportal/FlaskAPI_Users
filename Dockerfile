FROM python:3.10.6
# Run commands from /FlaskAPI_Users directory inside container
WORKDIR /FlaskAPI_Users_2
# Copy requirements from local to docker image
COPY requirements.txt /FlaskAPI_Users_2
# Install the dependencies in the docker image
RUN pip3 install -r requirements.txt --no-cache-dir
# Copy everything from the current dir to the image
COPY . .