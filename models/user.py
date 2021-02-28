#!/usr/bin/python3
"""Define user class"""

from models.base_model import BaseModel


class User(BaseModel):
    '''class user that inherit from BaseModel'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
