#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.  
import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv(dotenv_path=".env")
# sheety credentials

s_user = os.environ.get('username')
s_project = os.environ.get('projectName')
s_name = os.environ.get('sheetName')

s_endpoint = f'https://api.sheety.co/{s_user}/{s_project}/{s_name}'

s_response = requests.get(s_endpoint)
s_response.raise_for_status

pprint(s_response.json())