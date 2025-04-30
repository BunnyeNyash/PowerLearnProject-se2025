from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed


    @abstractmethod
    def move(self):
        pass


    @abstractmethod
    def fuel_type(self):
        pass


    def start_engine(self):
        return f"Starting {self.name}'s engine..."


    @property
    def describe(self):
        return f"{self.name} uses {self.fuel_type()} power."
    
    @property
    def vehicle_type(self):
        raise NotImplementedError("Must be implemented by all subclasses")



class Car(Vehicle):
    def move(self):
        return f"{self.name} moves silently on electricity."
    
    def fuel_type(self):
        return "Electricity"
    

class Bike(Vehicle):
    def move(self):
        return f"{self.name} zooms ahead on two wheels."

    def fuel_type(self):
        return "Petrol"

class ElectricScooter(Vehicle):
    def move(self):
        return f"{self.name} drives off-road with diesel power."

    def fuel_type(self):
        return "Diesel"
    

vehicles = [Car("Tesla", 110), Bike("Yamaha", 32), ElectricScooter("Jeep", 40)]

for vehicle in vehicles:
    print(vehicle.move())
    print(vehicle.describe)
    print(vehicle.start_engine())
    print("----------------------------")
