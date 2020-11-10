from ams_models.aircraft import Aircraft
import re
class AircraftManager:
    airplane = []
    def __init__(self):
        #Reading all data from the aircraft file
        with open("textFile/aircraft.txt", "rt") as airFile:
            for air in airFile.readlines():
                new_a = air.split()
                name =new_a[0]
                model=new_a[1]
                capacity=new_a[2]
                regNo=new_a[3]
                a = Aircraft(name, model, capacity, regNo)
                self.airplane.append(a)

    def createCraft(self, name, model, capacity, regNo):
        a = Aircraft(name, model, capacity, regNo)
        self.airplane.append(a)
        self.save()

        print(f'Aircraft {name} with REG-ID {regNo} was created successfully')

    def save(self):
        # Writing to a File
        with open("textFile/aircraft.txt", "w+") as airFile:
            for a in self.airplane:
                airFile.write(str(a))
                airFile.write("\n")

    def showCraft(self, a):
        print(a)

    def findCraftID(self, regNo):
        for a in self.airplane:
             if a.regNo == regNo:
                return a.regNo

    def findCraft(self, regNo):
        for a in self.airplane:
            if a.regNo == regNo:
                return a

    def printCraft(self):
        print(f'NAME    MODEL       CAPACITY    REGISTRATION-ID')
        for a in self.airplane:
            self.showCraft(a)


    def updateCraft(self, name, model, capacity, regNo):
        try:
            a = self.findCraft(regNo)
            a.name = name
            a.model = model
            a.capacity = capacity
            self.save()
            print(f"The craft with REG-ID:{regNo} was updated successfully!")
        except:
            print(f"No craft with the Registration-ID {regNo} exist")


    def retrieveCraft(self, regNo):
        a = self.findCraft(regNo)
        if a == False:
            print(f"No craft with the Registration-ID {regNo} exist")
        else:
            print(f'NAME    MODEL       CAPACITY    REGISTRATION-ID')
            return self.showCraft(a)


    def deleteCraft(self, regNo):
        try:
            a = self.findCraft(regNo)
            self.airplane.remove(a)
            self.save()
            print(f"The craft with REG-ID:{regNo} was deleted successfully!")
        except:
            print(f"No craft with the Registration-ID {regNo} exist")
