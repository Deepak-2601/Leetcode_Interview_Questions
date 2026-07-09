class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.slots = {1: big, 2: medium, 3: small}
    
    def addCar(self, carType):
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        else:
            return False
     
ParkingSystems = ParkingSystem(1, 1, 0)
print(ParkingSystems.addCar(1))
print(ParkingSystems.addCar(2))
print(ParkingSystems.addCar(3))