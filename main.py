from ams_service.aircraftManager import AircraftManager
from ams_service.flightManager import FlightManager
from ams_service.bookingManager import BookingManager
from ams_service.passengerManager import PassengerManager
import sys

aircraftmanager = AircraftManager()
flightmanager = FlightManager(aircraftmanager)
passengermanager = PassengerManager()
bookingmanager = BookingManager(passengermanager, flightmanager)


def main():
    flag = True
    while flag:
        mainmenu()
        command = input('Please input a command: ')
        if command == '0':
            flag = False
        else:
            subMenu(command)



# the exit button.
# AIRCRAFT MANAGEMENT SERVICE MENU - (MAIN MENU)
def mainmenu():
    print(
        '''
Press 0 to exit
Press 1 for AircraftManagement
Press 2 for FlightManagement
Press 3 for Passenger Management
Press 4 for Booking Management
'''
    )


# COMMAND LINE FOR SUBMENU
def subMenu(command):
    if command == '1':
        aircraftMenu()
        new_command = input('Please input a command to perform an operation: ')
        if new_command == '0':
            pass
        else:
            aircraftHandler(new_command)

    elif command == '2':
        flightMenu()
        new_command = input('Please input a command to perform an operation: ')
        if new_command == '0':
            pass
        else:
            flightHandler(new_command)

    elif command == '3':
        passengerMenu()
        new_command = input('Please input a command to perform an operation: ')
        if new_command == '0':
            pass
        else:
            passengerHandler(new_command)

    elif command == '4':
        bookingMenu()
        new_command = input('Please input a command to perform an operation: ')
        if new_command == '0':
            pass
        else:
            bookingHandler(new_command)


# AIRCRAFT MANAGEMENT SYSTEM SERVICE OPTION MENU (SUB-MENU)
def aircraftMenu():
    print(
        '''
Press 1 to add Aircraft
Press 2 to Search for an Aircraft
Press 3 to Update Aircraft
Press 4 to List Aircraft
Press 5 to Delete Aircraft
Press 0 to Go back to main menu
        '''
    )


def flightMenu():
    print('''
Press 1 to add Flight
Press 2 to Search for a Flight
Press 3 to Update Flight
Press 4 to List Flight
Press 5 to Delete Flight
Press 0 to go back to main menu
    ''')


def passengerMenu():
    print('''
Press 1 to add Passenger
Press 2 to Search for a Passenger
Press 3 to Update Passenger
Press 4 to List Passenger
Press 5 to Delete Passenger
Press 0 to go back to main menu
    ''')


def bookingMenu():
    print('''
Press 1 to add Booking
Press 2 to Search for a Booking
Press 3 to Update Booking
Press 4 to List Booking
Press 5 to Delete Booking
Press 0 to go back to main menu
    ''')


# AIRCRAFT MANAGEMENT SERVICE HANDLER
def aircraftHandler(new_command):
    if new_command == '1':
        name = input('Enter the name of aircraft: ')
        capacity = input('Enter aircraft capacity: ')
        model = input('Enter the aircraft model: ')
        regNo = input('Enter the registration number: ')
        aircraftmanager.createCraft(name, model, capacity, regNo)
    elif new_command == '2':
        regNo = input('Please input the registration number of aircraft to retrieve: ')
        aircraftmanager.retrieveCraft(regNo)
    elif new_command == '3':
        name = input('Enter the name of aircraft: ')
        capacity = input('Enter aircraft capacity: ')
        model = input('Enter the aircraft model: ')
        regNo = input('Enter the registration number: ')
        aircraftmanager.updateCraft(name, model, capacity, regNo)
    elif new_command == '4':
        aircraftmanager.printCraft()
    elif new_command == '5':
        regNo = input('Please input the registration number of aircraft to delete: ')
        aircraftmanager.deleteCraft(regNo)
    else:
        print('Your Input does not Exist')

    subMenu('1')


# FLIGHT MANGEMENT SERVICE HANDLER
def flightHandler(new_command):
    if new_command == '1':
        aircraft = input('Enter the registration number of the aircraft: ')
        takeoffLocation = input('Enter state of Departure: ')
        destination = input('Enter the arrival country: ')
        date = input('Enter the date of flight: ')
        time = input('Enter the time of flight: ')
        flightmanager.createFlight(aircraft, takeoffLocation, destination, date, time)

    elif new_command == '2':
        regNo = input('Please input the registration number of the airline to retrieve flight: ')
        flightmanager.retrieveFlight(regNo)

    elif new_command == '3':
        aircraft = input('Enter the registration number of the aircraft: ')
        takeoffLocation = input('Enter state of Departure: ')
        destination = input('Enter the arrival country: ')
        date = input('Enter the date of flight: ')
        time = input('Enter the time of flight: ')
        flightmanager.updateFlight(aircraft, takeoffLocation, destination, date, time)

    elif new_command == '4':
        flightmanager.printFlight()

    elif new_command == '5':
        aircraft = input('Please input the aircraft to delete flight: ')
        flightmanager.deleteFlight(aircraft)

    else:
        print('Your Input does not Exist')

    subMenu('2')


# PASSENGER MANAGEMENT SERVICE HANDLER
def passengerHandler(new_command):
    if new_command == '1':
        name = input('Enter the name of passenger: ')
        idNo = input('Enter the identification number: ')
        email = input('Enter the email: ')
        address = input('Enter the address: ')
        passengermanager.createUser(name, idNo, email, address)

    elif new_command == '2':
        idNo = input('Please input the Passenger-ID to retrieve details: ')
        passengermanager.retrieveUser(idNo)

    elif new_command == '3':
        name = input('Enter the name of Passenger: ')
        idNo = input('Enter the Passenger ID: ')
        email = input('Enter the email of the Passenger: ')
        address = input('Enter the address of the Passenger: ')
        passengermanager.updateUser(name, idNo, email, address)

    elif new_command == '4':
        passengermanager.printUser()

    elif new_command == '5':
        idNo = input('Please input the passenger id to delete: ')
        passengermanager.deleteUser(idNo)

    else:
        print('Your Input does not Exist')

    subMenu('3')


# BOOKING MANAGEMENT SERVICE HANDLER
def bookingHandler(new_command):
    if new_command == '1':
        passenger = input('Enter the passenger ID number: ')
        flight = input('Enter the flight aircraft registration number: ')
        ticketType = input('Enter the ticket type: ')
        ticketClass = input('Enter the ticket Class: ')
        bookingmanager.createBooking(passenger, flight, ticketType, ticketClass)

    elif new_command == '2':
        seatNumber = int(input('Please input the seat number to retrieve the booking for the passenger: '))
        bookingmanager.retrieveBooking(seatNumber)

    elif new_command == '3':
        passenger = input('Enter the passenger ID number: ')
        flight = input('Enter the flight aircraft registration number: ')
        ticketType = input('Enter the ticket type: ')
        ticketClass = input('Enter the ticket Class: ')
        seatNumber = input('Enter the passenger seat number: ')
        bookingmanager.updateBooking(passenger, flight, ticketType, ticketClass, seatNumber)

    elif new_command == '4':
        bookingmanager.printBooking()

    elif new_command == '5':
        seatNumber = input('Please input the passenger seat number to delete booking: ')
        bookingmanager.deleteBooking(seatNumber)

    else:
        print('Your Input does not Exist')

    subMenu('4')


main()
