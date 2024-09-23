# -*- coding: utf-8 -*-

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.errors = dict()

    def validate(self):
        if not self.username:
            self.errors['username'] = 'Username is required'
        if not self.password:
            self.errors['password'] = 'Password is required'

    def is_valid(self):
        self.validate()
        return not bool(self.errors)
