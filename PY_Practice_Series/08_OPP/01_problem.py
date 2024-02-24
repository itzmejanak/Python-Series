# 1. Basic Class and Object
# Problem: Create a `Car` class with attributes like `brand` and `model`. Then create an instance of this class.

# SOLUTION START:-

class Cars:
    def __init__(self, brand, model):
        self.brand  = brand
        self.model = model

my_car = Cars("lambo", "trx")
# print(my_car.brand)
# print(my_car.model)


my_new_car = Cars("Cambo", "ranbow")
# print(my_car.brand)
# print(my_car.model)

# SOLUTION END:-




















# 4. Encapsulation
# Problem: Modify the `Car` class to encapsulate the `brand` attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def fullName(self):
        return "The car brand is: " + self.__brand + "\nThe car model is: " + self.model

my_car = Car("Lambo", "TRX")
# print(my_car.fullName())

my_new_car = Car("Cambo", "Rainbow")
# print(my_new_car.fullName())


class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        # self.brand = brand
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = Electric_car("tesla", "model s", "700kw")
print(my_tesla.battery_size)
print(my_tesla.fullName())