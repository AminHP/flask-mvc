#!/usr/bin/env python
# -*- coding: utf-8 -*-
# find . -name \*.pyc -delete

# project imports
from project import app
from project.application import configure_app
from project.config import DeploymentConfig


configure_app(app, DeploymentConfig)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
