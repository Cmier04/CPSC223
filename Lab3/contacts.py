#Christine Mier
#September 22, 2024
#Contact List: using dictionary

def add_contact(contact_dict, /, *, id, first_name, last_name):
    '''Add first and last names to contact_dict'''
    if id in contact_dict:
        return print('Error: Contact already exists')
    else:
        contact_dict[id] = [first_name, last_name]
        return print(f'{first_name}, {last_name} has been added.')
    
def modify_contact(contact_dict, /, *, id, first_name, last_name):
    '''Modify contact and add new contact'''
    if id not in contact_dict:
        return print(f'Error: Invalid phone number.')
    else:
        first_name = input('Enter First Name: ')
        last_name = input('Enter Last Name: ')
        contact_dict[id] = [first_name, last_name]
        return print(f'{first_name}, {last_name} has been added.')

def delete_contact(contact_dict, /, *, id):
    '''Delete contact using id'''
    if id not in contact_dict:
        return print(f'Error')
    elif id.isdigit():
        del contact_dict[id]
        return print(f'{id} has been removed.')

def sort_contacts(contact_dict, /):
    '''Sort contact list by first name, then last name aphabetically'''
    dict(sorted(contact_dict.items(), key = lambda items:
                        (items[1][1], items[1][0])))
    return contact_dict

#Does not work: Does not sort and does not check input
def find_contact(contact_dict, /, *, find):
    '''find contact in dictionary and return'''
    found_contact = {}
    if isinstance(find, str) and find.isdigit() and find in contact_dict:
        found_contact[find] = contact_dict[find]
        found_contact[find]
    for key, value in contact_dict.items():
        first_name = value[0]
        last_name = value[1]
        if (find.lower() in first_name.lower()) or (find.lower() in last_name.lower()):
            found_contact[key] = value
    sorted_contacts = sort_contacts(found_contact)
    print(f'Found {first_name} {last_name}')
    return sorted_contacts

