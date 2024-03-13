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