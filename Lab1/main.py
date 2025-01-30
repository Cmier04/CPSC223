#Christine Mier
#September 9, 2024
#Main File for Contact List, Assignment 1
#Menu for Contact List

from contacts import*
import sys

contact_list = []
menu = 0

#while-loop to iterate through menu
while menu < 5:
    print('***Employee Contact Menu***')
    print('1. Print List\n2. Add Contact\n3. Modify Contact\n4. Delete Contact\n5. Exit the Program')
    menu = int(input('Pick a menu choice: '))
    if menu == 1:
        print_list(contact_list)
    elif menu == 2:
        add_contact(contact_list)
    elif menu == 3:
        modify_contact(contact_list)
    elif menu == 4:
        delete_contact(contact_list)
    elif menu == 5:
        print('**Exiting Program**')
        sys.exit()
    else:
        print('Invalid Menu Choice')
        print(print_list(contact_list))
