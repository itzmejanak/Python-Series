# 2. Class Method and Self
# Problem: Add a method to the `Car` class that displays the full name of the car (brand and model).

# SOLUTION START:-

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return "The car brand is: " + self.brand + "\nThe car model is: " + self.model

my_car = Car("Lambo", "TRX")
print(my_car.fullName())

my_new_car = Car("Cambo", "Rainbow")
print(my_new_car.fullName())

# SOLUTION END:-
