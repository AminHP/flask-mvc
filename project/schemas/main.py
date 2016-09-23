# -*- coding: utf-8 -*-

from good import Schema, Required


welcome = Schema({
    Required('name'): unicode
})
