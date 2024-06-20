from dotenv import load_dotenv
import requests
import os


load_dotenv('.env')
token = os.environ.get('TELEGRAM_TOKEN')
chat_id = os.environ.get('CHAT_ID')

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, best_flight):
        self.price = best_flight.price
        self.departure_code= best_flight.departure_code
        self.arrival_code = best_flight.destination_code
        self.out_date = best_flight.departure_day
        self.in_date = best_flight.return_day
        
    def send_message(self):
    
        text = f'Low price alert! {self.price}€ to fly from {self.departure_code} to {self.arrival_code} on {self.out_date} until {self.in_date}'
        end_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
        response = requests.get(end_url)
        response.raise_for_status()
        data = response.json()
        