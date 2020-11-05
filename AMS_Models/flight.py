class Flight:
    def __init__(self, aircraft, takeoffLocation, destination, date, time):
        self.aircraft = aircraft
        self.takeoffLocation = takeoffLocation
        self.destination = destination
        self.date = date
        self.time = time

    def __str__(self):
        return f" {self.aircraft} {self.takeoffLocation} {self.destination} {self.date} {self.time}"