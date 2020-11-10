class Aircraft:
    name: str
    model: str
    capacity: int
    regNo: str

    def __init__(self, name, model, capacity, regNo):
        self.name = name
        self.model = model
        self.capacity = capacity
        self.regNo = regNo

    def __str__(self):
        return f"{self.name:<8}{self.model:<13}{self.capacity:<12}{self.regNo}"