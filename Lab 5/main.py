#Christine Mier
#October 15, 2024
#Main module to Weather report program which creates and executes main menu in order to store and display weather data

import weather

def main():
    '''main function which creates and executes a main menu for weather.py'''
    filename = "weather_data.json"
    weather_data = {}

    while True:
        print(f'{"\n ":20}{"*** TUFFY TITAN WEATHER LOGGER MAIN MENU ***"}')
        print("1. Set data filename")
        print("2. Add weather data")
        print("3. Print daily report")
        print("4. Print historical report")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            filename = input("Enter filename: ")
            weather_data = weather.read_data(filename=filename)

        elif choice == '2':
            date = input("Enter date (YYYYMMDD): ")
            time = input("Enter time (hhmmss): ")
            try:
                temp = int(input("Enter temperature (ºC): "))
                humidity = int(input("Enter humidity (%): "))
                rainfall = float(input("Enter rainfall (mm): "))
                key = f'{date}{time}'
                weather_data[key] = {
                    't': temp,
                    'h': humidity,
                    'r': rainfall
                }
                weather.write_data(data = weather_data, filename = filename)
            except ValueError:
                print("Invalid input")

        elif choice == '3':
            date = input("Enter date (YYYYMMDD): ")
            report = weather.report_daily(data = weather_data, date = date)
            print(report)
        elif choice == '4':
            report = weather.report_historical(data = weather_data)
            print(report)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
