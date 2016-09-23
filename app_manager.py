# -*- coding: utf-8 -*-

# python imports
import os

# flask imports
from flask.ext.script import Manager

# project imports
from project import app
from project.application import configure_app
from project.config import DevelopmentConfig, DeploymentConfig, TestingConfig


manager = Manager(app)


@manager.command
def run():
    """
    Run server on port 8080 with default config.
    """
    app.run(host='0.0.0.0', port=8080)


@manager.command
def develop():
    """
    Run server on port 8080 with development config.
    """
    configure_app(app, DevelopmentConfig)
    app.run(host='0.0.0.0', port=8080)


@manager.command
def deploy():
    """
    Run server on port 8080 with deployment config.
    """
    configure_app(app, DeploymentConfig)
    app.run(host='0.0.0.0', port=8080)


@manager.command
def testing():
    """
    Run server on port 8080 with testing config.
    """
    configure_app(app, TestingConfig)
    app.run(host='0.0.0.0', port=8080)


@manager.option(dest='config_file')
def custom_config(config_file):
    """
    Run server on port 8080 with custom config file.
    """
    configure_app(app, os.path.abspath(config_file), is_pyfile=True)
    app.run(host='0.0.0.0', port=8080)


@manager.command
def celery():
    """
    Run celery worker.
    """
    from project.extensions import celery
    from celery.bin import worker
    worker = worker.worker(app=celery)
    worker.run()


@manager.option('-r', dest='resource', required=False, help='Resource name')
@manager.option('-u', dest='url', required=False, default='http://localhost:8080', help='Server url')
def test(resource, url):
    """
    Test api. You can specify a resource (like api_1.user) for single testing.
    By default all resources will be tested.
    """
    from tests import run
    run(url, resource)
