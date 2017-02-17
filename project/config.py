# -*- coding: utf-8 -*-

# python imports
import random
import string
import os


class DefaultConfig(object):
    # app

    DEFAULT_APP_NAME = 'project'
    DEBUG = True
    TESTING = True
    DEPLOYMENT = False
    TOKEN_EXPIRE_TIME = 3600

    # directory

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    TEMP_DIR = os.path.join(BASE_DIR, 'tmp')
    SCHEMA_DIR = os.path.join(BASE_DIR, 'schemas')

    # cache

    CACHE_TYPE = 'null'
    CACHE_DEFAULT_TIMEOUT = 900
    CACHE_THRESHOLD = 100
    CACHE_NO_NULL_WARNING = True
    CACHE_DIR = os.path.join(TEMP_DIR, 'Cache')

    # redis

    REDIS_URL = "redis://localhost:6379/0"

    # celery

    CELERY_BROKER_URL = REDIS_URL
    CELERY_RESULT_BACKEND = REDIS_URL

    # mongo

    MONGODB_SETTINGS = {
        'db': 'project',
        'host': '127.0.0.1',
        'port': 27017
    }

    # sqlalchemy

    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db.sqlite' % TEMP_DIR
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(DefaultConfig):
    # app

    TESTING = False

    # cache

    CACHE_TYPE = 'filesystem'


class DeploymentConfig(DefaultConfig):
    # app

    DEBUG = False
    DEPLOYMENT = True

    # cache

    CACHE_TYPE = 'redis'


class TestingConfig(DefaultConfig):
    # app

    DEBUG = True
    TESTING = True

    # cache

    CACHE_TYPE = 'filesystem'
