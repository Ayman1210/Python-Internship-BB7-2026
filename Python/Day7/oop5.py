class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15°C")
        self.__celsius = value

    @property
    def kelvin(self):
        return self.__celsius + 273.15


t = Temperature(25)

print("Celsius:", t.celsius)
print("Kelvin:", t.kelvin)

# Invalid temperature
try:
    t.celsius = -300
except ValueError as e:
    print("Error:", e)