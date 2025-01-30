#Christine Mier
#September 12, 2024
#Demonstrate the use of passing by value and passing by arguments

contact_list = []

def print_list(contact_list, /):
    '''Prints the Contact List input by user'''
    print('=' * 18, 'CONTACT LIST', '=' * 18)
    print(f'{"Index":8}{"First Name":22}{"Last Name":22}')
    print('=' * 5, '=' * 20, '=' * 18)
    for i in range(len(contact_list)):
       print(f'{str(i):8}{contact_list[i][0]:22}{contact_list[i][1]:22}')

def add_contact(contact_list, /, *, first_name, last_name):
    '''Adds Contact through user input to the contact list'''
    first_name = input('Enter first name: ')
    last_name = input('Enter Last name: ')
    #add if statements to ensure input is not empty and not an integer
    if first_name == '' or first_name.isdigit():
        print('Invalid input')
    elif last_name == '' or last_name.isdigit():
        print('Invalid input')
    else:
        contact_list.append([first_name, last_name])

def modify_contact(contact_list, /, *, first_name, last_name, index):
    '''Modifies Contact at given index and checks for invalid input'''
    index = int(input('Modify Index # '))
    if index < 0 or index > len(contact_list):
        print('Invalid Input')
        return False
    else:
        first_name = input('Enter First Name: ')
        last_name = input('Enter Last Name: ')
        if first_name == '' or first_name.isdigit():
            print('Invalid input')
        elif last_name == '' or last_name.isdigit():
            print('Invalid input')
        else:
            contact_list[index] = [first_name, last_name]
            print(f'Index {index} has been modified to {first_name}, {last_name}.')
        return True

def delete_contact(contact_list,/, *, index):
    '''Deletes contact at given index and validates input'''
    index = int(input('Delete Index # '))
    if index < 0 or index > len(contact_list) or ValueError:
        print('Invalid Input')
        return False
    else:
        deleted_contact = contact_list.pop(index)
        print(f'Contact {deleted_contact[0]} {deleted_contact[1]} at index {index} deleted.')
        return True

def sort_contacts(contact_list, /, *, column):
    '''sorts contact list by first name or last name alphabetically'''
    if column == 0:
        contact_list.sort(key = lambda contact: contact[column])
    if column == 1:
        contact_list.sort(key = lambda contact: contact[column])
        


    
    
    
