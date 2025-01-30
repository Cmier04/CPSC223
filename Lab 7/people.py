#Christine Mier
#5 November 2024
#Program utilizes classes, functions, and instance variables to implement a Faculty and Student list

class Person:
    '''Declares first and last name variables and serves as the parent class'''
    def __init__(self, first_name, last_name, /):
        self.firstname = first_name
        self.lastname = last_name

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Faculty(Person):
    '''Declares a faculty which coincides with faculty list and inherits from Person class'''
    def __init__(self, first_name, last_name, department, /):
        super().__init__(first_name, last_name)
        self.department = department

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
class Student(Person):
    '''Student class corresponds to student list in main module and inherits from Parent class'''
    def __init__(self, firstname, lastname, /):
        super().__init__(firstname, lastname)
        self.class_year = None
        self.major = None
        self.advisor = None

    def set_class(self, class_year, /):
        self.class_year = class_year

    def set_major(self, major, /):
        self.major = major

    def set_advisor(self, faculty, /):
        self.advisor = faculty

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
