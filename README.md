# flask-mvc-framework
---------------------

A mini MVC framework using flask.
This project is a fork of [salimane/flask-mvc](https://github.com/salimane/flask-mvc)



### Features:
>* Support different API versions for controllers and schemas. 
>* Very fast json validation using `good`.
>* Run and install server in virtual environment automatically.
>* Update requirements automatically
>* Restful API documentation using [Flassger](https://github.com/rochacbruno/flasgger)
>* Restful API testing using [pyresttest](https://github.com/svanoort/pyresttest)


### Installation:

```
$ sudo pip install virtualenv
$ sudo apt-get install docker (for deploying)
```

### Run server:
Run these commands in separate shells.


```
$ python manager.py celery
$ python manager.py run
```

### Test api:
Run these commands in separate shells.

```
$ python manager.py testing
$ python manager.py test
```


### Deploy server:

```
$ sudo service docker start
$ cd deploy
$ ./deploy.sh
```

### Apidoc:

> [http://localhost:8080/apidocs/index.html](http://localhost:8080/apidocs/index.html)

