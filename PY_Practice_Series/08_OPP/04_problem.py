# 4. Encapsulation
# Problem: Modify the `Car` class to encapsulate the `brand` attribute, making it private, and provide a getter method for it.

# 2. Class Method and Self

class Car:
    def __init__(self, brand, model):
        self.__brand = brand                # changes here
        self.model = model

    def fullName(self):
        return "The car brand is: " + self.__brand + "\nThe car model is: " + self.model

    def get_brand(self):                # CHANGES HERE  and learn setter by yourself
        return self.__brand
    
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
# print(my_tesla.battery_size)
# print(my_tesla.fullName())
# print(my_tesla.__brand)            # its give us error we cannot access directly to variable           
print(my_tesla.get_brand())          # changes here and accessing through method




# 4. Encapsulation
                                    # OVERVIEW HERE ABOVE CHANGES

def __init__(self, brand, model):
        self.__brand = brand                # changes here by privating the variables
        self.model = model

def fullName(self):
        return "The car brand is: " + self.__brand + "\nThe car model is: " + self.model

def get_brand(self):                # CHANGES HERE  and learn setter by yourself
        return self.__brand

# print(my_tesla.__brand)            # its give us error we cannot access directly to variable           
print(my_tesla.get_brand()) 