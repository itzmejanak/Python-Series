# 6. Class Variables
# Problem: Add a class variable to `Car` that keeps track of the number of cars created.

class Car:
    total_car = 0;
    def __init__(self, brand, model):
        self.__brand = brand                
        self.model = model
        Car.total_car += 1

    def fullName(self):
        return "The car brand is: " + self.__brand + "\nThe car model is: " + self.model

    def get_brand(self):                
        return self.__brand
    
    def fule_type(self):            # CHANGES HERE FOR POLY
        return "Petrol or Diseal"
    
my_car = Car("Lambo", "TRX")
# print(my_car.fullName())
my_new_car1 = Car("car1", "brand1")
my_new_car = Car("Cambo", "Rainbow")
# print(my_new_car.fullName())

# print(my_car.total_car)              # wrong approach
print(Car.total_car)                   # right approach