#Christine Mier
#29 October 2024
#This program creates, modifies, deletes, sorts, and prints a contact list
#This is the main file which loops through the main menu of the Contact list

from contacts import Contacts
import sys

def main():
    '''main function which holds the while loop for the main menu'''
    filename = 'contacts.json'
    contact_list = Contacts(filename = filename)

    while True:
        '''While loop pringts main menu and loops through it'''
        print('\n**** TUFFY TITAN CONTACT MAIN MENU ***')
        print('1. Add Contact')
        print('2. Modify Contact')
        print('3. Delete Contact')
        print('4. Print Contact List')
        print('5. Set Contact Filename')
        print('6. Exit The Program')
        choice = input('Enter menu choice: ')
        
        if choice == '1':
            id = input('Enter Phone Number: ')
            first_name = input('Enter First Name: ')
            last_name = input('Enter Last Name: ')
            result = contact_list.add_contact(id = id, first_name = first_name, last_name = last_name)
            if isinstance(result, dict):
                print(f'Added: {first_name} {last_name}.')
            else:
                print(result)

        elif choice == '2':
            id = input('Enter Phone Number: ')
            first_name = input('Enter First Name: ')
            last_name = input('Enter Last Name: ')
            modified = contact_list.modify_contact(id = id, first_name = first_name, last_name = last_name)
            if isinstance(modified, dict):
                print(f'Modified: {first_name} {last_name}.')
            else:
                print(modified)
        elif choice == '3':
            id = input('Enter Phone Number: ')
            deleted = contact_list.delete_contact(id = id)
            if isinstance(deleted, dict):
                print(f'Deleted: {deleted}')
            else:
                print(deleted)
        elif choice == '4':
            if not contact_list.data:
                print('No contacts found.')
            else:
                print('=' * 18, 'CONTACT LIST', '=' *18)
                print(f'{"Last Name":19}{"First Name":21}{"Phone":19}')
                print('=' * 18, '=' * 20, '=' * 10)
                for id, names in contact_list.data.items():
                    print(f'{names[1]:<22} {names[0]:<19} {id}')
        elif choice == '5':
            filename = input('Enter new filename: ')
            contact_list = Contacts(filename = filename)
            print(f'Contact List Filename Set to: {filename}')

        elif choice == '6':
            print('Exiting Program')
            sys.exit()
            
        else:
            print('Invalid choice. Please Try Again')
            continue

if __name__ == '__main__':
    main()
            
        
