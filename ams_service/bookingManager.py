from ams_models.booking import Booking
class BookingManager():
    bookings = []
    def __init__(self, passengerManager, flightManager):
        self.passengerManager = passengerManager
        self.flightManager = flightManager

    def createBooking(self, passenger, flight, ticketType, ticketClass):
        idNo = self.passengerManager.findUser(passenger)
        aircraft = self.flightManager.findFlight(flight)
        if idNo == None and aircraft == None:
            print('There is no booking for this passenger!')
        else:
            booking = Booking(passenger, flight, ticketType, ticketClass)
            self.bookings.append(booking)
            print(f'A booking for {idNo} with {aircraft} was made')

    def showBooking(self, booking):
        print(booking)

    def findBooking(self, passenger):
        for booking in self.bookings:
            if booking.passenger == passenger:
                return booking

    def retrieveBooking(self, passenger):
        retrieve = self.findBooking(passenger)
        return self.showBooking(retrieve)

    def updateBooking(self, passenger, flight, ticketType, ticketClass):
        update = self.findBooking(passenger)
        update.flight = flight
        update.ticketType = ticketType
        update.ticketClass = ticketClass

    def deleteBooking(self, passenger):
        delete = self.findBooking(passenger)
        return self.bookings.remove(delete)

    def printBooking(self):
        for booking in self.bookings:
            return self.showBooking(booking)

