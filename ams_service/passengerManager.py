from ams_models.passenger import Passenger
class PassengerManager:
    user = []
    def createUser(self, name, idNo, email, address):
        passenger = Passenger(name, idNo, email, address)
        self.user.append(passenger)

    def showUser(self, passenger):
        print(passenger)

    def findUser(self, idNo):
        for passenger in self.user:
            if passenger.idNo == idNo:
                return passenger

    def retrieveUser(self, idNo):
        retrieve = self.findUser(idNo)
        return self.showUser(retrieve)

    def updateUser(self, name, idNo, email, address):
        update = self.findUser(idNo)
        update.name = name
        update.email = email
        update.address = address

    def deleteUser(self, idNo):
        delete = self.findUser(idNo)
        return self.user.remove(delete)

    def printUser(self):
        print(f'NAME        PASSENGER-ID       ADDRESS      EMAIL')
        for passenger in self.user:
            return self.showUser(passenger)

