# Solution file
class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    pass

class ElectricCar(Car):
    pass

obj = ElectricCar()
obj.move()