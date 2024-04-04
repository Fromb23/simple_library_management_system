#!/usr/bin/python3

from base_class import BaseClass

class Admin(BaseClass):
    def __init__(self, first_name, last_name, username, email, date_of_birth, user_id, password):
        new_user = BaseClass(first_name, last_name, username, email, date_of_birth, user_id, password)
        return new_user
