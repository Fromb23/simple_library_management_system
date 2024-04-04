#!/usr/bin/python3

import uuid

class BaseClass():
    def __init__(self, first_name, last_name, username, email, date_of_birth, user_id, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.date_of_birth = date_of_birth
        self.email = email
        self.__user_id = uuid.uuid4()
        self.password = password

    def get_usernames(self):
        return self.first_name, self.last_name

    @property
    def get_id(self):
        return self.__id

    @user_id.setter
    def user_id(self):
        return self.__user_id

    def login(self, username, password):
        if username == self.username and password == self.password:
            self.is_login = True
        else:
            return "Invalid username or password"

    def logout(self, is_login):
        self.is_login = False
