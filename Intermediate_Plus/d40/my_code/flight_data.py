
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,origin,dest,from_date,to_date,stops):
        self.price=price
        self.origin=origin
        self.dest=dest
        self.from_date=from_date
        self.to_date=to_date
        self.stops=stops

def cheapest(flight_data):
    if flight_data is None:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A","N/A")
    first_flight = flight_data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    nr_stops = len(first_flight["itineraries"][0]["segments"]) - 1
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price,origin,destination,out_date,return_date,nr_stops)

    for flight in flight_data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date,nr_stops)

    return cheapest_flight
