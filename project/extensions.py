# -*- coding: utf-8 -*-

# flask extentions
from flask.ext.cache import Cache
from flask.ext.celery import Celery
from flask.ext.redis import FlaskRedis
from flask.ext.mongoengine import MongoEngine
from flask.ext.sqlalchemy import SQLAlchemy

# project extentions
from project.modules.schema_validator import Validator
from project.modules.api_router import ApiRouter
from project.modules.api_doc import ApiDoc


cache = Cache()
celery = Celery()
redis = FlaskRedis()
mongodb = MongoEngine()
sqldb = SQLAlchemy()
validator = Validator()
api_router = ApiRouter()
api_doc = ApiDoc()
