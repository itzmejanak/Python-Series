# 10. Multiple Inheritance
# Problem: Create two classes `Battery` and `Engine`, and let the `ElectricCar` class inherit from both, demonstrating multiple inheritance.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand                
        self.model = model

    def fullName(self):
        return "The car brand is: " + self.__brand + "\nThe car model is: " + self.model

    def get_brand(self):                
        return self.__brand
    
    def fule_type(self):           
        return "Petrol or Diesel"
    
my_car = Car("Lambo", "TRX")

my_new_car = Car("Cambo", "Rainbow")


class Battery:
    def batteryinfo(self):   # CHANGES HERE FOR multiple inheritance
        return "This is battery."


class Engine:
    def engineinfo(self):    # CHANGES HERE FOR multiple inheretance
        return "This is engine."


class Electric_car(Battery, Engine, Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fule_type(self):       
        return "Electric Charge"
    
my_tesla = Electric_car("tesla", "model s", "700kw")

print("my_tesla fuel type:", my_tesla.fule_type())

print(my_tesla.batteryinfo())   # Corrected method name
print(my_tesla.engineinfo())    # Note: engineinfo() method belongs to Engine class
