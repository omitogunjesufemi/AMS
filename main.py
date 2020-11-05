from ams_service.aircraftManager import AircraftManager
from ams_service.flightManager import FlightManager
from ams_service.bookingManager import BookingManager
from ams_service.passengerManager import PassengerManager

aircraftmanager = AircraftManager()
flightmanager = FlightManager(aircraftmanager)
passengermanager = PassengerManager()
bookingmanager = BookingManager(passengermanager, flightmanager)

def main():
    flag = True
    while flag:
        mainmenu()
        command = input('please input a command: ')
        subMenu(command)
        if command == 0:
            flag = False


#AIRCRAFT MANAGEMENT SERVICE MENU - (MAIN MENU)
def mainmenu():
    print(
'''
press 0 to exit
press 1 for AircraftManagement
press 2 for FlightManagement
press 3 for Passenger Management
press 4 for Booking Management
'''
    )
#COMMAND LINE FOR SUBMENU
def subMenu(command):
    if command == '1':
        aircraftMenu()
        new_command = input('please input a command to perform an operation')
        if new_command == '0':
            mainmenu()
        else:
            aircraftHandler(new_command)

    elif command == '2':
        flightMenu()
        new_command = input('please input a command to perform an operation')
        if new_command == '0':
            mainmenu()
        else:
            flightHandler(new_command)

    elif command == '3':
        passengerMenu()
        new_command = input('please input a command to perform an operation')
        if new_command == '0':
            mainmenu()
        else:
            passengerHandler(new_command)

    elif command == '4':
        bookingMenu()
        new_command = input('please input a command to perform an operation')
        if new_command == '0':
            mainmenu()
        else:
            bookingHandler(new_command)


#AIRCRAFT MANAGEMENT SYSTEM SERVICE OPTION MENU (SUB-MENU)
def aircraftMenu():
    print(
        '''
press 1 to add Aircraft
press 2 to Update Aircraft
press 3 to List Aircraft
press 4 to Delete Aircraft
press 0 to Go back to main menu
        '''
    )

def flightMenu():
    print('''
press 1 to add Flight
press 2 to Update Flight
press 3 to List Flight
press 4 to Delete Flight
press 0 to go back to main menu
    ''')

def passengerMenu():
    print('''
press 1 to add Passenger
press 2 to Update Passenger
press 3 to List Passenger
press 4 to Delete Passenger
press 0 to go back to main menu
    ''')

def bookingMenu():
    print('''
press 1 to add Booking
press 2 to Update Booking
press 3 to List Booking
press 4 to Delete Booking
press 0 to go back to main menu
    ''')


#AIRCRAFT MANAGEMENT SERVICE HANDLER
def aircraftHandler(new_command):
    if new_command == '1':
        name = input('enter the name of aircraft: ')
        capacity = input('enter aircraft capacity: ')
        model = input('enter the aircraft model: ')
        regNo = input('enter the registration number: ')
        aircraftmanager.createCraft(name, model, capacity, regNo)
    elif new_command == '2':
        name = input('enter the name of aircraft: ')
        capacity = input('enter aircraft capacity: ')
        model = input('enter the aircraft model: ')
        regNo = input('enter the registration number: ')
        aircraftmanager.updateCraft(name, model, capacity, regNo)
    elif new_command == '3':
        aircraftmanager.printCraft()
    elif new_command == '4':
        regNo = input('please input the registration number of aircraft to delete: ')
        aircraftmanager.deleteCraft(regNo)
    else:
        print('Your Input does not Exist')

    subMenu('1')

#FLIGHT MANGEMENT SERVICE HANDLER
def flightHandler(new_command):
    if new_command == '1':
        aircraft = input('Enter the registration number of the aircraft: ')
        takeoffLocation = input('enter state of Departure: ')
        destination = input('enter the arrival country: ')
        date = input('enter the date of flight: ')
        time = input('enter the time of flight: ')
        flightmanager.createFlight(aircraft, takeoffLocation, destination, date, time)

    elif new_command == '2':
        aircraft = input('Enter the registration number of the aircraft: ')
        takeoffLocation = input('enter state of Departure: ')
        destination = input('enter the arrival country: ')
        date = input('enter the date of flight: ')
        time = input('enter the time of flight: ')
        flightmanager.updateFlight(aircraft, takeoffLocation, destination, date, time)

    elif new_command == '3':
        flightmanager.printFlight()

    elif new_command == '4':
        aircraft = input('please input the aircraft to delete flight: ')
        flightmanager.deleteFlight(aircraft)

    else:
        print('Your Input does not Exist')

    subMenu('2')

#PASSENGER MANAGEMENT SERVICE HANDLER
def passengerHandler(new_command):
    if new_command == '1':
        name = input('enter the name of passenger: ')
        idNo = input('enter the identification number: ')
        email = input('enter the email: ')
        address = input('enter the address: ')
        passengermanager.createUser(name, idNo, email, address)

    elif new_command == '2':
        name = input('enter the name of a: ')
        idNo = input('enter state of Departure: ')
        email = input('enter the arrival country: ')
        address = input('enter the date of flight: ')
        passengermanager.updateUser(name, idNo, email, address)

    elif new_command == '3':
        passengermanager.printUser()

    elif new_command == '4':
        idNo = input('please input the passenger id to delete: ')
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
        passenger = input('Enter the passenger ID number: ')
        flight = input('Enter the flight aircraft registration number: ')
        ticketType = input('Enter the ticket type: ')
        ticketClass = input('Enter the ticket Class: ')
        bookingmanager.updateBooking(passenger, flight, ticketType, ticketClass)

    elif new_command == '3':
        bookingmanager.printBooking()

    elif new_command == '4':
        idNo = input('please input the passenger id to delete: ')
        bookingmanager.deleteBooking(idNo)

    else:
        print('Your Input does not Exist')

    subMenu('4')


main()