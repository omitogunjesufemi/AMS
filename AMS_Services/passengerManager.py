from AMS_Models.passenger import Passenger


class PassengerManager(Passenger):
    def __init__(self, create, retrieve, update, delete, printAll):
        self.__create = create
        self.__retrieve = retrieve
        self.__update = update
        self.__delete = delete
        self.__printAll = printAll

    def createUser(self, create):  # set
        pass

    def retrieveUser(self, retrieve):  # get
        pass

    def updateUser(self, update):  # set
        pass

    def deleteUser(self, delete):  # set
        pass

    def printUser(self, delete):  # get
        pass
