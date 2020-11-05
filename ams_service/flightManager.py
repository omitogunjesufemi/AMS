from ams_models.flight import Flight
from ams_service.aircraftManager import AircraftManager

class FlightManager:
    flights = []
    def __init__(self, ams):
        self.ams: AircraftManager = ams



    def createFlight(self, aircraft, takeoffLocation, destination, date, time):
        regNo = self.ams.findCraft(aircraft)
        if regNo == None:
            print('The aircraft does not exist')
            return False
        else:
            flight = Flight(aircraft, takeoffLocation, destination, date, time)
            self.flights.append(flight)
            #flightNumber = f"{takeoffLocation}/{destination}/{date}"
            print(f'Flight with {regNo} was created')

    def showFlight(self, flight):
        print(f"The flight is for {flight.aircraft} from {flight.takeoffLocation} to {flight.destination} on {flight.date},{flight.time}")

    def findFlight(self, aircraft):
        for flight in self.flights:
            if flight.aircraft == aircraft:
                return flight

    def retrieveFlight(self, aircraft):
        retrieve = self.findFlight(aircraft)
        return self.showFlight(retrieve)

    def updateFlight(self, aircraft, takeoffLocation, destination, date, time):
        update = self.findFlight(aircraft)
        update.takeoffLocation = takeoffLocation
        update.destination = destination
        update.date = date
        update.time = time

    def deleteFlight(self, aircraft):
        delete = self.findFlight(aircraft)
        return self.flights.remove(delete)

    def printFlight(self):
        for flight in self.flights:
            return self.showFlight(flight)


# booking = flightManager()
# booking.createFlight()
#
# booking.printFlight()