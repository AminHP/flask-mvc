# -*- coding: utf-8 -*-

# python imports
import os

# flask imports
from flask import Flask

# project imports
from config import DefaultConfig


def create_app():
    app = Flask(__name__)
    configure_app(app, DefaultConfig)
    configure_extensions(app)
    return app


def configure_app(app, config, is_pyfile=False):
    if is_pyfile:
        app.config.from_pyfile(config)
    else:
        app.config.from_object(config)

    [os.makedirs(v) for k, v in app.config.items() if k.endswith('DIR') and not os.path.exists(v)]


def configure_extensions(app):
    from project import extensions

    for extension in dir(extensions):
        try:
            attr = getattr(extensions, extension)
            if not isinstance(attr, type) and 'init_app' in dir(attr):
                attr.init_app(app)
        except AttributeError as e:
            print e
