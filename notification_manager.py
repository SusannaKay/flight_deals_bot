from dotenv import load_dotenv
import requests
import os
import smtplib


load_dotenv('.env')
token = os.environ.get('TELEGRAM_TOKEN')
chat_id = os.environ.get('CHAT_ID')
my_email = os.environ.get('my_email')
password = os.environ.get('password')

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, best_flight):
        self.price = best_flight.price
        self.departure_code= best_flight.departure_code
        self.arrival_code = best_flight.destination_code
        self.out_date = best_flight.departure_day
        self.in_date = best_flight.return_day
        self.stop = best_flight.stop
        
        
    def send_message(self):
    
        text = f'Low price alert! {self.price}€ to fly from {self.departure_code} to {self.arrival_code} on {self.out_date} until {self.in_date}'
        end_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
        response = requests.get(end_url)
        response.raise_for_status()
        data = response.json()
    
    def send_email(self, to_email):
        text = f'Subject:Low price alert!\n\n Price Drop: {self.price}EUR to fly from {self.departure_code} to {self.arrival_code}, with {self.stop} stop(s) on {self.out_date} until {self.in_date}'
       
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=text
            )
