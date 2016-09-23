# -*- coding: utf-8 -*-

from good import Schema, All, Required, Length, Match, Email


signup = Schema({
    Required('username'): All(unicode, Match(r'^[a-zA-Z0-9_]+$')),
    Required('email'): Email(),
    Required('password'): All(unicode, Length(min=5))
})
