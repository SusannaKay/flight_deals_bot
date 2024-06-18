#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.  
from data_manager import DataManager
from pprint import pprint

sheet = DataManager()
sheet_data = sheet.read_file() ## dictionaries list

pprint(sheet_data)
