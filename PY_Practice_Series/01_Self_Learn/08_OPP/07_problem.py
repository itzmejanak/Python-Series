# 7. Static Method
# Problem: Add a static method to the `Car` class that returns a general description of a car.

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
    
    def fule_type(self):           
        return "Petrol or Diseal"
    
    # Decorator
    @staticmethod        # by using this and removing self we can access by it class name at line no:- 35
    def general_dec():
        return "Cars are means of transport"
    
my_car = Car("Lambo", "TRX")
# print(my_car.fullName())
my_new_car1 = Car("car1", "brand1")
my_new_car = Car("Cambo", "Rainbow")
# print(my_new_car.fullName())

# print(my_car.total_car)             
# print(Car.total_car)                   

# print(my_new_car.general_dec())         # We use static keyword for to not access that static var/method except the own class

print(Car.general_dec())  # now it will work