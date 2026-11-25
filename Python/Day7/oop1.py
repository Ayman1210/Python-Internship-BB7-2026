class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"My car is {self.brand} {self.model}, "
              f"manufactured in {self.year}.")


# Creating 3 objects
car1 = Car("Toyota", "Fortuner", 2022)
car2 = Car("Honda", "City", 2023)
car3 = Car("Tata", "Nexon", 2024)

# Calling methods
car1.display_info()
car2.display_info()
car3.display_info()