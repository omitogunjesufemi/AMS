class Booking:
    def __init__(self, passenger, flight, ticketType, ticketClass):
        self.passenger = passenger
        self.flight = flight
        self.ticketType = ticketType
        self.ticketClass = ticketClass

    def __str__(self):
        return f"{self.passenger:<8s}{self.flight:<13s}{self.ticketType:<12s}{self.ticketClass}"