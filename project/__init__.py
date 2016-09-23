# -*- coding: utf-8 -*-

from application import create_app

app = create_app()

from project.controllers import *
