import json
import os

class Flights:
    def __init__(self, filename, /):
        self.filename = filename
        self.data_list = []
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.data_list = json.load(file)
            except FileNotFoundError:
                print(f'File {self.filename} not found. Starting with empty data.')
                return {}
    def add_flight(self, origin, destination, flight_number, departure, next_day, arrival, /):
        if not self._is_valid_time_format(departure) or not self._is_valid_time_format(arrival):
            return False
        flight = {
            'origin': origin,
            'destination': destination,
            'flight_number': flight_number,
            'departure': departure,
            'next_day': next_day,
            'arrival': arrival
        }
        self.data_list.append(flight)
        slef._write_data_to_file()
        return True
    def get_flights(self, /):
        flights_format = []
        for flight in self.data:
            departure = self._format_time(flight['departure'])
            arrival = self._format_time(flight['arrival'], ['next_day'])
            duration = slef._calculate_duration(flight['departure'], flight['arrival'],flight['next_day'])
        flights_format.append(f"{flight['origin']} {flight['destination']} {flight['flight_number']} {flight['next_day']}"
                              f"{departure} {arrival} {duration}")
        
            
            
    
        
            
