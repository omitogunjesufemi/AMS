class Passenger:
    def __init__(self, name, idNo, email, address):
        self.name = name
        self.idNo = idNo
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name:<12s}{self.idNo:<19s}{self.address:<13s}{self.email}"