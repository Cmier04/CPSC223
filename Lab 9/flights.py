#Christine Mier
#December 3, 2024
#This file creates and maintains a json file for a flight schedule and interacts with 'main.py'

import json
from datetime import datetime

class Flights:
    '''class which contains __init__, add_flight, get_flights'''
    def __init__(self, filename):
        self.filename = filename
        self.data = []

        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Starting with an empty schedule.")
    
    def add_flight(self, origin, destination, flight_number, departure, next_day, arrival):
        '''adds flight information to flight and writes information into json file'''
        try:
            departure_time = datetime.strptime(departure, "%H%M")
            arrival_time = datetime.strptime(arrival, "%H%M")
        except ValueError:
            return False
        
        flight = {
            "origin": origin,
            "destination": destination,
            "flight_number": flight_number,
            "departure": departure,
            "next_day": next_day,
            "arrival": arrival,
        }

        self.data.append(flight)

        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

        return True
    
    def get_flights(self):
        '''formats flight into a schedule and checks the time format is correct'''
        flight_schedule = []
        
        for flight in self.data:
            departure = datetime.strptime(flight["departure"], "%H%M").strftime("%I:%M%p").lower().lstrip("0")
            arrival = datetime.strptime(flight["arrival"], "%H%M").strftime("%I:%M%p").lower().lstrip("0")
            
            if flight["next_day"] == "Y":
                arrival = "+" + arrival
            
            duration_hours = (int(flight["arrival"]) - int(flight["departure"])) // 100
            duration_minutes = (int(flight["arrival"]) - int(flight["departure"])) % 100
            duration = f"{duration_hours}:{duration_minutes:02}"

            flight_schedule.append({
                "origin": flight["origin"],
                "destination": flight["destination"],
                "flight_number": flight["flight_number"],
                "departure": departure,
                "arrival": arrival,
                "duration": duration,
            })
        
        return flight_schedule
