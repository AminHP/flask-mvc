# -*- coding: utf-8 -*-

from good import Schema, Required


signup = Schema({
    Required('username'): unicode,
    Required('password'): unicode
})
