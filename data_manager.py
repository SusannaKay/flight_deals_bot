import requests
import os
from dotenv import load_dotenv



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv(dotenv_path=".env")
        
        self.s_username = os.environ.get('username')
        self.s_projectName = os.environ.get('projectName')
        self.s_sheetPrice = os.environ.get('sheetPrice')
        self.s_sheetUsers = os.environ.get('sheetUsers')
        self.s_endpoint_price = f'https://api.sheety.co/{self.s_username}/{self.s_projectName}/{self.s_sheetPrice}'
        self.s_endpoint_users = f'https://api.sheety.co/{self.s_username}/{self.s_projectName}/{self.s_sheetUsers}'

        self.s_header = {
            'Content-Type': 'application/json'
        }

        

    def read_file(self):
        s_response = requests.get(self.s_endpoint_price)
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
        row_endpoint = f'{self.s_endpoint_price}/{city['id']}'

        response = requests.put(url=row_endpoint, 
                                headers=self.s_header,
                                json=sheet_row)
        response.raise_for_status()
    
    def get_customer_email(self):
        s_response = requests.get(self.s_endpoint_users)
        s_response.raise_for_status
        email_list = []
        for subs in s_response.json()['users']:
            email_list.append(subs['email'])

        return email_list