from ams_models.flight import Flight
from ams_service.aircraftManager import AircraftManager

class FlightManager:
    flights = []
    def __init__(self, ams):
        self.ams: AircraftManager = ams
        with open("textFile/flight.txt", "rt") as flightFile:
            for flight in flightFile.readlines():
                new_flight = flight.split()
                aircraft = new_flight[0]
                takeoffLocation = new_flight[1]
                destination = new_flight[2]
                date = new_flight[3]
                time = new_flight[4]
                flight = Flight(aircraft, takeoffLocation, destination, date, time)
                self.flights.append(flight)

    def save(self):
        with open("textFile/flight.txt", "w+") as flightFile:
            for flight in self.flights:
                flightFile.write(str(flight))
                flightFile.write("\n")

    def createFlight(self, aircraft, takeoffLocation, destination, date, time):
        regID = self.ams.findCraftID(aircraft)
        regNo = self.ams.findCraft(aircraft)
        if regNo == None:
            print('The aircraft does not exist')
            return False
        else:
            flight = Flight(aircraft, takeoffLocation, destination, date, time)
            self.flights.append(flight)
            self.save()
            print(f'Flight with {regID} was created')

    def showFlight(self, flight):
        print(flight)

    def findFlight(self, aircraft):
        for flight in self.flights:
            if flight.aircraft == aircraft:
                return flight

    def findFlightID(self, aircraft):
        for flight in self.flights:
            if flight.aircraft == aircraft:
                return flight.aircraft

    def retrieveFlight(self, aircraft):
        retrieve = self.findFlight(aircraft)
        if retrieve == False:
            print(f"No flight with the Aircraft {aircraft} exist")
        else:
            print(f'AIRCRAFT-ID       DEPARTURE       DESTINATION        DATE        TIME')
            return self.showFlight(retrieve)

    def updateFlight(self, aircraft, takeoffLocation, destination, date, time):
        try:
            update = self.findFlight(aircraft)
            update.takeoffLocation = takeoffLocation
            update.destination = destination
            update.date = date
            update.time = time
            self.save()
            print("The Flight'\s details were updated successfully!")
        except:
            print("No Flight with the Aircraft-ID exist")

    def deleteFlight(self, aircraft):
        try:
            delete = self.findFlight(aircraft)
            self.flights.remove(delete)
            self.save()
            print(f"The Flight with Aircraft Details:{aircraft} was deleted successfully!")
        except:
            print(f"No Flight with the Aircraft Details:{aircraft} exist")

    def printFlight(self):
        print(f'AIRCRAFT-ID       DEPARTURE       DESTINATION        DATE        TIME')
        for flight in self.flights:
            self.showFlight(flight)
