from flights import Flights
import sys

filename = ''
flight_list = Flights(filename)

def main():
    while True:
        print(' ' * 5, '*** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU')
        print('1. Add Flight')
        print('2. Print Flight Schedule')
        print('3. Set Flight Schedule Filename')
        print('4. Exit Program')
        choice = input('Enter Menu Choice: ')

        if choice == '1':
            origin = input('Enter Origin: ')
            destination = input('Enter Destination: ')
            flight_number = input('Enter Flight Number: ')
            departure = input('Enter Departure Time (HHMM): ')
            arrival = input('Enter Arrival Time (HHMM): ')
            next_day = input('Is Arrival Next Day (Y/N): ')
            flight = Flights(origin, destination, flight_number, departure, arrival, next_day)
            flight_list.add_flight(flight)

        elif choice == '2':
            print('=' *18, 'FLIGHT SHCEDULE', '='*18)
            print('Origin Destination Number Departure  Arrival Duration')
            print('='*6, ' ', '='*11, ' ', '='*6, ' ', '='*6, '  ', '='*7, ' ', '='*8)
            for index, flight in enumerate(flight_list):
                print(f'{index:<10} {flight.origin} {flight.destination:<10} {flight.flight_number:<10} {flight.departure:<10} {flight.arrival:<10} {flight.next_day<10}')

        elif choice == '3':
            filename = input('Enter File Name: ')

        elif choice == '4':
            print('Exiting the program.')
            break
        else:
            print('Invalid Menu Choice. Please Try Again.')
if __name__ == '__main__':
    main()

