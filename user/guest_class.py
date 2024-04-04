#!/usr/bin/python3

from base_class import BaseClass
from storage.database import file_storage

class guest(BaseClass):
    def request_account(self):
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.date_of_birth = input("Enter date of birth: ")
        self.password = input("Enter your desired password: ")
        self.username = input("Enter your desired username: ")

        user_info = DataManager()
        user_info.insert_guest_requests(self.first_name, self.last_name, self.date_of_birth, self.password, self.username)
