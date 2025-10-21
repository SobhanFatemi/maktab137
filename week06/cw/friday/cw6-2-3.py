class Car:
    def __init__(self, car_id, model, year, is_available):
        self.car_id = car_id
        self.model = model
        self.year = year
        self.is_available = is_available

    def rent_car(self):
        if self.is_available:
            print(f"You rented: {self.model}")
            self.is_available = False
        else:
            print(f"{self.model} is not available!")
    
    def return_car(self):
        if not self.is_available:
            print(f"You returned: {self.model}")
            self.is_available = True
        else:
            print(f"{self.model} is not being rented!")

    def display_info(self):
        print(f"Car ID: {self.car_id}\nModel: {self.model}\nYear: {self.year}\nAvailability: {self.is_available}")
    

class RentalAgency():
    def __init__(self, cars=[]):
        self.cars = cars

    def add_car(self, *args):
        for arg in args:
            if arg in args:
                print(f"{arg.model} already exists!")
                self.cars.append(arg)
                print(f"{arg.model} was added!")

    def find_car(self, id):
        found = False
        for car in self.cars:
            if car.car_id == id:
                found = True
                print(car.model)
        if not found:
            print("Car not found!")

    def rent_car(self, car):
        car.rent_car()
    def return_car(self, car):
        car.return_car()
    
    def display_info(self, car):
        car.display_info()

samand = Car(347198, "Soren", 1391, True)
peugeot = Car(859303, "206", 1390, True)
        
agency = RentalAgency()
agency.add_car(samand, peugeot)
agency.find_car(347198)
agency.find_car(859303)
agency.rent_car(samand)
agency.display_info(samand)