class Car:
    def __init__(self, brand, model):
        self.__brand = brand                
        self.__model = model           # CHANGES HERE 

    def fullName(self):
        return "The car brand is: " + self.__brand + "\nThe car model is: " + self.__model

    def get_brand(self):                
        return self.__brand
    
    def fule_type(self):            
        return "Petrol or Diseal"
    
    @property
    def model(self):         # Changes here :- name of def should mention by exact variable name
        return self.__model
    
my_car = Car("Lambo", "TRX")
# print(my_car.fullName())
my_new_car = Car("Cambo", "Rainbow")
# print(my_new_car.fullName())

# From here:
# Attempting to change the model
my_car.model = "City"  # This should raise an AttributeError since model is read-only
print(my_car.fullName())  # Print the result to see if any changes occurred
