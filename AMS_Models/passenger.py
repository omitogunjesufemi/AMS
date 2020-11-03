class Passenger:

    print('done')
    def __init__(self, name, email, address):
        self.__name = name
        self.__email = email
        self.__address = address

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setAddress(self, address):
        self.__address = address

    def getAddress(self):
        return self.__address
