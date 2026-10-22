
class Car():                                  #Car= class
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")              #my_car = 0bject 
print(my_car.brand)   
print(my_car.model)

my_car_new = Car("Tata", "Safari")
print(my_car_new.brand)   
print(my_car_new.model)
