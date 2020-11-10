from ams_models.booking import Booking
class BookingManager:
    bookings = []
    seatList = []

    def __init__(self, passengerManager, flightManager):
        self.passengerManager = passengerManager
        self.flightManager = flightManager
        with open("textFile/booking.txt", "rt") as bookingFile:
            for booked in bookingFile.readlines():
                new_booking = booked.split()
                passenger = new_booking[0]
                flight = new_booking[1]
                ticketType = new_booking[2]
                ticketClass = new_booking[3]
                seatNumber = int(new_booking[4])
                self.seatList.append(seatNumber)
                booking = Booking(passenger, flight, ticketType, ticketClass, seatNumber)
                self.bookings.append(booking)



    def save(self):
        with open("textFile/booking.txt", "w+") as bookingFile:
            for booking in self.bookings:
                bookingFile.write(str(booking))
                bookingFile.write("\n")


    def createBooking(self, passenger, flight, ticketType, ticketClass):
        name = self.passengerManager.findUserName(passenger)
        regNo = self.flightManager.findFlightID(flight)
        passID = self.passengerManager.findUserID(passenger)
        idNo = self.passengerManager.findUser(passenger)
        aircraft = self.flightManager.findFlight(flight)
        if idNo == None or aircraft == None:
            print('This passenger cannot be booked a flight as it has no PASS-ID or assigned flight!')
        else:
            taken_seat = self.seatList[-1]
            self.seatNumber = taken_seat + 1
            ticketID = (f"{passID}/{regNo}/{self.seatNumber}")
            booking = Booking(passenger, flight, ticketType, ticketClass, self.seatNumber)
            self.bookings.append(booking)
            self.save()
            print(f"""A booking for {name} with Flight-ID:{regNo} was made.
                      Your seat number is {self.seatNumber}. The Ticket ID is {ticketID}""")

    def showBooking(self, booking):
        print(booking)

    def findBooking(self, seatNumber):
        self.seatNumber = seatNumber
        for booking in self.bookings:
            if booking.seatNumber == seatNumber:
                return booking

    def retrieveBooking(self, seatNumber):
        self.seatNumber = seatNumber
        retrieve = self.findBooking(seatNumber)
        if retrieve == None or retrieve == False:
            print(f"No Booking with the seat number: {seatNumber} exist")
        else:
            return self.showBooking(retrieve)

    def updateBooking(self, passenger, flight, ticketType, ticketClass, seatNumber):
        self.seatNumber = seatNumber
        try:
            update = self.findBooking(seatNumber)
            update.passenger = passenger
            update.flight = flight
            update.ticketType = ticketType
            update.ticketClass = ticketClass
            self.save()
            print("The Booking details were updated successfully!")
        except:
            print(f"No Booking with the seat number: {seatNumber} exist")

    def deleteBooking(self, seatNumber):
        self.seatNumber = seatNumber
        try:
            delete = self.findBooking(seatNumber)
            self.bookings.remove(delete)
            self.save()
            print(f"The Booking with the seat number: {seatNumber} was deleted successfully!")
        except:
            print(f"No Booking with the seat number: {seatNumber}  exist")

    def printBooking(self):
        print(f'PASGR-ID        AIRCRAFT-ID       TICKET-TYPE      TICKET-CLASS      SEAT-NUMBER')
        for booking in self.bookings:
            self.showBooking(booking)

