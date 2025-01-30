#Christine Mier
#December 3, 2024
#This program is the main file to 'flights.py' which implements a main menu

import sys
from flights import Flights

def main():
    '''Main menu which allows user input for a flight schedule'''
    filename = "flights_schedule.json"
    flight_list = Flights(filename)

    while True:
        print("\n     *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU")
        print("1. Add Flight")
        print("2. Print Flight Schedule")
        print("3. Set Flight Schedule Filename")
        print("4. Exit The Program")

        choice = input("Enter menu choice: ")

        if choice == '1':
            '''add_flight'''
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            flight_number = input("Enter flight number: ")
            departure = input("Enter departure time (HHMM): ")
            arrival = input("Enter arrival time (HHMM): ")
            next_day = input("Next day arrival? (Y/N): ")

            success = flight_list.add_flight(origin, destination, flight_number, departure, next_day, arrival)
            if success:
                print("Flight added successfully!")
            else:
                print("Error: Invalid time format. Please ensure the times are in HHMM format.")
        
        elif choice == '2':
            '''get_flight'''
            print('=' *18, 'FLIGHT SHCEDULE', '='*18)
            print('Origin Destination Number Departure  Arrival Duration')
            print('='*6, '='*11, '='*6, '='*9, '='*8, '='*8)
            flights = flight_list.get_flights()
            for flight in flights:
                print(f'{flight["origin"]:<10} {flight["destination"]:<7} {flight["flight_number"]:<6} {flight["departure"]:<9} {flight["arrival"]:<8} {flight["duration"]}')

        elif choice == '3':
            '''__init__'''
            filename = input("Enter new filename: ")
            flight_list = Flights(filename)
            print(f'Flight schedule file set to: {filename}')

        elif choice == '4':
            print("Exiting the program.")
            sys.exit()

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
