# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method `fuel_type` in both `Car` and `ElectricCar` classes, but with different behaviors.

# 2. Class Method and Self with encapsulation

class Car:
    def __init__(self, brand, model):
        self.__brand = brand                
        self.model = model

    def fullName(self):
        return "The car brand is: " + self.__brand + "\nThe car model is: " + self.model

    def get_brand(self):                
        return self.__brand
    
    def fule_type(self):            # CHANGES HERE FOR POLY
        return "Petrol or Diseal"
    
my_car = Car("Lambo", "TRX")
# print(my_car.fullName())

my_new_car = Car("Cambo", "Rainbow")
# print(my_new_car.fullName())



# 3. Inheritance with encapsulation
class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        # self.brand = brand
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fule_type(self):        # CHANGES HERE FOR POLY
        return "Electric Charge"
    
my_tesla = Electric_car("tesla", "model s", "700kw")
# print(my_tesla.battery_size)
# print(my_tesla.fullName())

# print(my_tesla.__brand)                      
# print(my_tesla.get_brand())          

print("my_car fuel type:", my_car.fule_type())
print("my_tesla fuel type:", my_tesla.fule_type())