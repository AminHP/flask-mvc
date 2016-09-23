FROM tiangolo/uwsgi-nginx:python2.7

MAINTAINER Flask-MVC <mdan.hagh@gmail.com>

# Add app configuration to Nginx
RUN openssl req -x509 -newkey rsa:2048 -keyout /etc/ssl/mycert.key -out /etc/ssl/mycert.crt -days XXX -nodes -subj "/C=US/ST=New York/L=Brooklyn/O=Example Brooklyn Company/CN=examplebrooklyn.com"

# Copy app
COPY . /app
COPY deploy /app
COPY deploy/nginx.conf /etc/nginx/conf.d/

# Install requirements
WORKDIR /app
RUN pip install -r requirements
