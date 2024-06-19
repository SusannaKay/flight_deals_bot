#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.  
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

sheet = DataManager()
sheet_data = sheet.read_file() ## dictionaries list

#{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54}
flights = FlightSearch()
for city in sheet_data:
    if city['iataCode'] == '':
        updateIata = FlightSearch()

        city['iataCode'] = updateIata.changeIata(city)
        sheet.update_file(city)
    
    
    get_offer = flights.get_flights(city)
    

        


        

