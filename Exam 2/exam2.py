#Christine Mier
#05 November 2024

class MyTypeError(Exception):
    '''Does not work'''
    pass

class Person:
    def __init__(self, first_name, last_name, gender, age):
        if not isinstance(age, int):
            raise MyTypeError('Age must be an integer')
        if gender != 'Male' and gender != 'Female':
            raise MyTypeError('Gender must be Male or Female.')
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def GetName(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
         return f'Person: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}'

class CSUF_Student(Person):
    count = 0
    school = 'CSUF'
    def __init__(self, first_name, last_name, gender, age, ID, major):
        super().__init__(first_name, last_name, gender, age)
        CSUF_Student.count += 1
        self.ID = ID
        self.major = major
        if not isinstance(ID, int):
            raise MyTypeError('ID must be an integer')
    def instance(self):
        return self.ID
    def ChangeMajor(major):
        self.major = new_major
    def __str__(self):
        person_str = super().__str__()
        return f'{person_str}, ID: {self.ID}, Major: {self.major}'

