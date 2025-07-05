# -*- coding: utf-8 -*-
from dataclasses import dataclass, field


@dataclass(frozen=True)
class User:
    username: str
    password: str
    errors: dict = field(
        default_factory=dict, init=False, hash=False, compare=False
    )

    def __post_init__(self):
        if not self.username:
            self.errors['username'] = 'Username is required'
        if not self.password:
            self.errors['password'] = 'Password is required'

    def is_valid(self):
        return not bool(self.errors)
