#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.  
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
import time

origin = 'ROM'

sheet = DataManager()
sheet_data = sheet.read_file() ## dictionaries list

#{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54}
flights = FlightSearch()
for city in sheet_data:
    # if city['iataCode'] == '':
    #     updateIata = FlightSearch()

    #     city['iataCode'] = updateIata.changeIata(city)
    #     sheet.update_file(city)
    
    
    best_flight = flights.get_flights(city, is_direct=True)

    if best_flight == None:
        best_flight = flights.get_flights(city, origin=origin, is_direct=False)
        

    if city['lowestPrice'] > best_flight.price:
        message = NotificationManager(best_flight)
        message.send_message()
        customer_list = sheet.get_customer_email()
        for email in customer_list:
            message.send_email(email)

       
        
    
    time.sleep(2)
    

        


        

