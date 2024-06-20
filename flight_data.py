

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
            
            self.price = float(flight['price']['total'])
            
            if best_price != 0 and self.price < best_price:
                best_price = self.price
                self.departure_day = flight['itineraries'][0]['segments'][0]['departure']['at'].split("T")[0]
                self.return_day = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                self.destination_code = flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
                
                
            elif best_price == 0:
                best_price = self.price
                
            
            
            
        return best_price

