
# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

# Child class
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

# Grandchild class
class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Speed:", self.speed, "km/h")

# Create object
s = SportsCar("BMW", "M4", 250)

s.display()
