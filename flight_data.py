

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.price = 0
        self.departure_code = 'ROM'
        self.destination_code = ''
        self.departure_day=''
        self.return_day=''


        
    
    def find_chepest_flight(self, data):
        best_price = 0

        for flight in data:
            
            ticket_price = float(flight['price']['total'])
            
            if best_price != 0:
                if ticket_price < best_price:
                    self.price = best_price
                    self.departure_day = flight['itineraries'][0]['segments'][0]['departure']['at'].split("T")[0]
                    self.return_day = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                    self.destination_code = flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
                    
                
                
            else:
                best_price = ticket_price
                self.price = ticket_price
                self.departure_day = flight['itineraries'][0]['segments'][0]['departure']['at'].split("T")[0]
                self.return_day = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                self.destination_code = flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
                
            
            
            
        return self

