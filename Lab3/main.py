#Christine Mier
#September 22, 2024
#Main Script which Contains a Main Menu and user prompts for Contact Dictionary

from contacts import*
import sys

contact_dict = {}

while True:
    '''While loop prints main menu and loops through it'''
    try:
        print('***Employee Contact Menu***')
        print('1. Add Contact\n2. Modify Contact\n3. Delete Contact\n4. Print Contact List\n5. Find Contact\n6. Exit The Program')
        menu = input('Pick a menu choice: ')
        if menu == '1':
            id = input('Enter Phone Number: ')
            first_name = input('Enter First Name: ')
            last_name = input('Enter Last Name: ')
            add_contact(contact_dict, id = id, first_name = first_name,
                        last_name = last_name)
    #Error: Does not work, revert to first_name = first_name and prompt for input within function
        elif menu == '2':
            id = input('Enter Phone Number: ')
            modify_contact(contact_dict, id = id, first_name = first_name,
                           last_name = last_name)
        elif menu == '3':
            id = input('Enter Phone Number: ')
            delete_contact(contact_dict, id = id)
        elif menu == '4':
            print('=' * 18, 'CONTACT LIST', '=' * 18)
            print(f'{"Last Name":19}{"First Name":21}{"Phone":19}')
            print('=' * 18, '=' * 20, '=' * 10)
            for k,v in contact_dict.items():
                print(f'{v[1]:19}{v[0]:21}{k:22}')
        elif menu == '5':
            find = input('Enter Phone Number: ')
            find_contact(contact_dict, find = find)
        elif menu == '6':
            print('**Exiting Program***')
            sys.exit()
        else:
            print('Invalid')
            continue
    except ValueError:
        print('Invalid Input')
        pass
