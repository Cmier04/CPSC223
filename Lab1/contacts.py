#Christine Mier
#September 5, 2024
#Contact List Function Definitions

contact_list = []
first = ''
last = ''

#prints header of list and formats the list
def print_list(contact_list):
    '''Prints the Contact List input by user'''
    print('=' * 18, 'CONTACT LIST', '=' * 18)
    print(f'{"Index":8}{"First Name":22}{"Last Name":22}')
    print('=' * 5, '=' * 20, '=' * 18)
    for i in range(len(contact_list)):
       print(f'{str(i):8}{contact_list[i][0]:22}{contact_list[i][1]:22}')

#adds contact to list
def add_contact(contact_list):
    '''Adds contscts to the list'''
    first = input('First Name: ')
    last = input('Last Name: ')
    if first == '':
        print('Invalid input.')
    elif last == '':
        print('Invalid input.')
    else:
        contact_list.append([first, last])
    return contact_list

#modifies contact at provided index
def modify_contact(contact_list):
    '''Modifies the contact list'''
    index = int(input('Modify index #'))
    if index < 0 or index > len(contact_list):
        print('Error: Invalid index.')
        return contact_list
    first = input('Enter First Name: ')
    last = input('Enter Last Name: ')
    if first == '':
        print('Invalid input.')
    elif last == '':
        print('Invalid input.')
    else:
        contact_list[index] = [first, last]
        print(f'Index {index} has been modified to {first}, {last}.')
    return contact_list

#Deletes element of list from index provided by user
def delete_contact(contact_list):
    '''Deletes contact from list'''
    index = int(input('Delete contact #'))
    print('Number entered ', index)
    if index < 0 or index >= len(contact_list):
        print('Invalid index. No contact deleted.')
        return contact_list
    deleted_contact = contact_list.pop(index)
    print(f'Contact {deleted_contact[0]} {deleted_contact[1]} at index {index} deleted.')
    return contact_list
