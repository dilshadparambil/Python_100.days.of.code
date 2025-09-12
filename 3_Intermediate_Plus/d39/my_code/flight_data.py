
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,origin,dest,from_date,to_date):
        self.price=price
        self.origin=origin
        self.dest=dest
        self.from_date=from_date
        self.to_date=to_date

def cheapest(flight_data):
    if flight_data is None:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
    first_flight_price=float(flight_data['data'][0]["price"]["grandTotal"])
    cheapest_flight = FlightData(first_flight_price,'','','','')

    for flight in flight_data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price <= first_flight_price:
            first_flight_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(first_flight_price, origin, destination, out_date, return_date)

    return cheapest_flight
