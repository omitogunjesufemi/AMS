from ams_models.passenger import Passenger
class Booking:
    def __init__(self, passenger, flight, ticketType, ticketClass, seatNumber):
        self.passenger = passenger
        self.flight = flight
        self.ticketType = ticketType
        self.ticketClass = ticketClass
        self.seatNumber = seatNumber


    def __str__(self):
        return f"{self.passenger:<16}{self.flight:<19}{self.ticketType:<17}{self.ticketClass:<18}{self.seatNumber}"