import requests
import os
from dotenv import load_dotenv



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv(dotenv_path=".env")
        self.s_user = os.environ.get('username')
        self.s_project = os.environ.get('projectName')
        self.s_name = os.environ.get('sheetName')
        self.s_endpoint = f'https://api.sheety.co/{self.s_user}/{self.s_project}/{self.s_name}'
        self.s_header = {
            'Content-Type': 'application/json'
        }

        

    def read_file(self):
        s_response = requests.get(self.s_endpoint)
        s_response.raise_for_status

        return s_response.json()['prices']
    def update_file(self, city):
        sheet_row = {
            'price':{
                'city': city['city'],
                'iataCode': city['iataCode'],
                'lowestPrice': city['lowestPrice']
            }
        }
        row_endpoint = f'{self.s_endpoint}/{city['id']}'

        response = requests.put(url=row_endpoint, 
                                headers=self.s_header,
                                json=sheet_row)
        response.raise_for_status()
