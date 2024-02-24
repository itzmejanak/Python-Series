# 3. Inheritance
# Problem: Create an `ElectricCar` class that inherits from the `Car` class and has an additional attribute `battery_size`.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return "The car brand is: " + self.brand + "\nThe car model is: " + self.model

my_car = Car("Lambo", "TRX")
# print(my_car.fullName())

my_new_car = Car("Cambo", "Rainbow")
# print(my_new_car.fullName())



# 3. Inheritance
class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        # self.brand = brand
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = Electric_car("tesla", "model s", "700kw")
print(my_tesla.battery_size)
print(my_tesla.fullName())
