import requests
import os
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime, timedelta
from flight_data import FlightData

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
TOKEN_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'
OFFERS_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        load_dotenv(dotenv_path=".env")
        self._api_key = os.environ.get('AMA_KEY')
        self._api_secret = os.environ.get('AMA_SECRET')
        self._token = self.get_new_token()
        
    def get_new_token(self):
        header ={
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body ={
            'grant_type':'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(
            url=TOKEN_ENDPOINT,
            headers=header,
            data=body
            )
        return response.json()['access_token']


    def changeIata (self, city):

        parameters = {
            'keyword': city['city'],
            'max':2,
            'include':'AIRPORTS'
        }
        header ={
            'Authorization': f'Bearer {self._token}'
        }
        response = requests.get(url=IATA_ENDPOINT,headers= header,params=parameters)
        response.raise_for_status()
        try:
            code = response.json()['data'][0]['iataCode']
        except IndexError:
            return "N/A"
        except KeyError:
            return "not found"
        
       
        return code
    
    def get_flights(self, city, origin, is_direct= True):
        tomorrow = datetime.today() + timedelta(days=1)
        return_date = tomorrow + timedelta(days=7)
        header_flight ={
            'Authorization': f'Bearer {self._token}'
        }
        if is_direct:
            parameters = {
                'originLocationCode':origin,
                'destinationLocationCode': city['iataCode'],
                'departureDate': tomorrow.strftime('%Y-%m-%d'),
                'returnDate': return_date.strftime('%Y-%m-%d'),
                'adults': 1,
                'nonStop': 'true',
                'currencyCode': 'EUR',
                'max':10
            }
        else:
            parameters = {
                'originLocationCode':origin,
                'destinationLocationCode': city['iataCode'],
                'departureDate': tomorrow.strftime('%Y-%m-%d'),
                'returnDate': return_date.strftime('%Y-%m-%d'),
                'adults': 1,
                'nonStop': 'false',
                'currencyCode': 'EUR',
                'max':10
            }

        print(f"Getting flights for {city['city']}...")
        
        response = requests.get(url=OFFERS_ENDPOINT, 
                                params=parameters, headers=header_flight)
        try: 
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"HTTPError: {e}")
            print(f"Response text: {response.text}")
            raise
        
        data = response.json()['data']
        
        if not data:
            print(f'No direct flights to {city['city']}. Looking for 2 stop itineraries...')

        else:

            check = FlightData(origin)
            best_flight = check.find_chepest_flight(data)
            
            print(f'{city['city']}: {best_flight.price}€')
            return best_flight

       