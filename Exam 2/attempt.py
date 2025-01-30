class MyTypeError(Exception):
    """Custom exception class to handle specific type errors."""
    pass

class Person:
    def __init__(self, first_name, last_name, gender, age):
        # Check if age is an integer
        if not isinstance(age, int):
            raise MyTypeError('Age must be an integer')
        
        # Check if gender is either 'Male' or 'Female'
        if gender != 'Male' and gender != 'Female':
            raise MyTypeError('Gender must be Male or Female.')
        
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def get_name(self):
        # Return the full name by combining first and last name
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        # Return a string representation of the person
        return f'Person: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}'


# Example with incorrect gender input
person = Person("Alice", "Bob", 'c', 12)  # This will raise MyTypeError because gender is invalid
