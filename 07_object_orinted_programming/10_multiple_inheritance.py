

class Car():  

    total_car = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
         return self.__brand + "!" 
          
          

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "cars are means of transport"

    @property
    def model(self):
         return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
             super().__init__(brand,model)
             self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

    
    
    

# my_tesla = ElectricCar("Tesla", "Model S", "85 kwh") 

# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))

# my_car = Car("Tata", "Safari")
# #my_car.model = "city"
# Car("Tata", "Nexon")

# print(my_car.model)

class battery:
     def battery_info(self):
          return "this is battery"
     

class engine:
     def engine_info(self):
          return "this is engine"
     
    

class ElectricCarTwo(battery,engine,Car):
     pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())