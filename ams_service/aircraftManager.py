from ams_models.aircraft import Aircraft
class AircraftManager:
    airplane = []
    def createCraft(self, name, model, capacity, regNo):
        a = Aircraft(name, model, capacity, regNo)
        self.airplane.append(a)
        print(f'Aircraft {name} is created successfully')

    def showCraft(self, a):
        print(a)

    def findCraft(self, regNo):
        for a in self.airplane:
            if a.regNo == regNo:
                return a

    def printCraft(self):
        print(f'NAME    MODEL       CAPACITY    REGISTRATION-ID')
        for a in self.airplane:
            return self.showCraft(a)

    def updateCraft(self, name, model, capacity, regNo):
        a = self.findCraft(regNo)
        a.name = name
        a.model = model
        a.capacity = capacity

    def retrieveCraft(self, regNo):
        a = self.findCraft(regNo)
        return self.showCraft(a)

    def deleteCraft(self, regNo):
        a = self.findCraft(regNo)
        return self.airplane.remove(a)

