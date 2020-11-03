from ams_models.passenger import Passenger

user = []


class PassengerManager(Passenger):
    def __init__(self, create, retrieve, update, delete, printAll):
        super().__init__()
        self.__create = create
        self.__retrieve = retrieve
        self.__update = update
        self.__delete = delete
        self.__printAll = printAll

    def createUser(self, name, email, address):
        user.append(name)
        user.append(email)
        user.append(address)

    def retrieveUser(self):  # get
        return user

    def updateUser(self, name, email, address):
        pass

    def deleteUser(self):
        return user.clear()

    def printUser(self):
        return user
