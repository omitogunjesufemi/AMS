class Flight:
    def __init__(self, aircraft, takeoffLocation, destination, date, time):
        self.aircraft = aircraft
        self.takeoffLocation = takeoffLocation
        self.destination = destination
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.aircraft:18s}{self.takeoffLocation:16s}{self.destination:19s}{self.date:12s}{self.time}"