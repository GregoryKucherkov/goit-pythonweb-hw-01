from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.brand} {self.model}: The engine is started")

class Motorcycle(Vehicle):

    def start_engine(self):
        print(f"{self.brand} {self.model}: Brrrr.. The engine is started")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, brand: str, model: str):
        pass

    @abstractmethod
    def create_motorcycle(self, brand: str, model: str):
        pass

class USVehicleFactory(VehicleFactory):

    def create_car(self, brand: str, model: str ):
        car = Car(brand, model)
        print(f"US Spec {brand} {model} is created")
        return car

    def create_motorcycle(self, brand: str, model: str):
        motorcycle = Motorcycle(brand, model)
        print(f"US Spec {brand} {model} is created")
        return motorcycle

class EUVehicleFactory(VehicleFactory):

    def create_car(self, brand: str, model: str ):
        car = Car(brand, model)
        print(f"EU Spec {brand} {model} is created")
        return car

    def create_motorcycle(self, brand: str, model: str):
        motorcycle = Motorcycle(brand, model)
        print(f"EU Spec {brand} {model} is created")
        return motorcycle
    

if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    us_car = us_factory.create_car("Ford", "Mustang")
    eu_car = eu_factory.create_car("Mercedes", "E-class")

    us_car.start_engine()
    eu_car.start_engine()

    us_moto = us_factory.create_motorcycle("Harley", "Sportster")
    eu_moto = eu_factory.create_motorcycle("Ducati", "Diavel")

    us_moto.start_engine()
    eu_moto.start_engine()




