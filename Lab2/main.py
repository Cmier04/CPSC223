#Christine Mier
#September 12 2024
#Main script for Employee Contact List

from contacts import*
import sys

contact_list = []
menu = 0
first_name = ''
last_name = ''
index = 0

while True:
    '''While loop prints main menu'''
    try:
        print('***Employee Contact Menu***')
        print('1. Print List\n2. Add Contact\n3. Modify Contact\n4. Delete Contact\n5. Sort by First Name\n6. Sort by Last Name\n7. Exit the program')
        menu = int(input('Pick a menu choice: '))
        if menu == 1:
            print_list(contact_list)
        elif menu == 2:
            add_contact(contact_list, first_name = first_name,
                        last_name = last_name)
        elif menu == 3:
            modify_contact(contact_list, first_name = first_name,
                           last_name = last_name, index = index)
        elif menu == 4:
            delete_contact(contact_list, index = index)
        elif menu == 5:
            sort_contacts(contact_list, column = 0)
        elif menu == 6:
            sort_contacts(contact_list, column = 1)
        elif menu == 7:
            print('**Exiting Program**')
            sys.exit()
        elif menu < 1 or menu > 7:
            print('Invalid Menu Choice')
            continue
    except ValueError:
        print('Invalid Input')
        pass
