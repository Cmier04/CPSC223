#Christine Mier
#29 October 2024
#This program creates, modifies, deletes, sorts, and prints a contact list

import json
import os

class Contacts:
    def __init__(self, /, *, filename):
        '''opens, reads, and creates the .json file which stores the Contact List'''
        self.filename = filename
        self.data = {}
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.data = json.load(file)
            except FileNotFoundError:
                print('File not found')
                
    def add_contact(self, /, *, id, first_name, last_name):
        '''Add Names and Phone numbers to Contact List'''
        if id in self.data:
            return 'Error: Contact already exists.'
        self.data[id] = [first_name, last_name]
        self.data = dict(sorted(self.data.items(), key = lambda item: (item[1][1].lower(), item[1][0].lower())))
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
        return {id: self.data[id]}
    
    def modify_contact(self, /, *, id, first_name, last_name):
        '''modify existing contact in contact list and adds it to the list'''
        if id not in self.data:
            return 'Error'
        self.data[id] = [first_name, last_name]
        self.data = dict(sorted(self.data.items(), key = lambda item: (item[1][1].lower(), item[1][0].lower())))
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
        return {id: self.data[id]}
    
    def delete_contact(self, /, *, id):
        '''deletes pre-existing contact from contact list'''
        if id not in self.data:
            return 'Error'
        deleted_contact = {id: self.data.pop(id)}
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
        return deleted_contact
