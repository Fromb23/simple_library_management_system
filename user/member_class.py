#!/usr/bin/python3

from base_class import BaseClass

class member(BaseClass):
    def update_information(self, new_email=None, new_password=None):
        if new_password:
            self.password = new_password
        if new_email:
            self.email = new_email
