from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed  # triggering the setter for encapsulated attribute


    @property
    def max_speed(self):
        return self.__max_speed # will return the max_speed value
    
    @max_speed.setter       # changing speed
    def max_speed(self, speed):
        if speed < 0:
            raise ValueError("Speed CANNOT be negative")
        self.__max_speed = speed
    
    
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
        return f"{self.name} uses {self.fuel_type()} power and runs on a maximum speed of {self.max_speed} km\\hr."



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
    

vehicles = []

vehicle_data = [
    (Car, "Tesla", 110),
    (Bike, "Yamaha", 32),
    (ElectricScooter, "Jeep", -40)
]

# to prevent the setter from crashing the entire program due to a user's invalid input
for _, name, max_speed in vehicle_data:
    try:
        vehicles.append(_(name, max_speed))
    
    except ValueError as e:
        print(f"\nWarning: {e} for {name}. Skipping this vehicle.\n")



for vehicle in vehicles:
    print(vehicle.move())
    print(vehicle.describe)
    print(vehicle.start_engine())
    print("----------------------------")
