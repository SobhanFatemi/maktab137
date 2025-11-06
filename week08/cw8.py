from datetime import datetime

class Car:
    def __init__(self, plate_number: str, model: str, battery_level: int = 100, milage:float = 0.0 , status: str = "available"):
        self.plate_number = plate_number
        self.model = model
        self.battery_level = max(0, min(100, int(battery_level)))
        self.milage = milage
        self.status = status

    def check_battery(func):
        def wrapper(self, *args, **kwargs):
            if self.battery_level < 20:
                print(f"Battery level is low: {self.battery_level}, charging now!")
                self.charge(100-self.battery_level)
            else:
                return func(self, *args, **kwargs)
        return wrapper
    
    @check_battery
    def drive(self, km: float) -> None:
        if km <= 0:
            return
        if self.status == "Charging":
            raise RuntimeError("Car is charging.")
        required_battery = km * 0.2
        self.milage += km
        self.battery_level = max(0, self.battery_level - required_battery)
        self.status = "On_Trip"

    def charge(self, amount: float) -> None:
        if amount <= 0:
            return
        self.battery_level = min(100, self.battery_level + amount)
        self.status = "Charging" if self.battery_level < 100 else "Available"

    def __str__(self) -> str:
        return f"{self.model} [{self.plate_number}] - {self.milage} Km, {self.battery_level}% Battery, status: {self.status}"

    def __eq__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.plate_number == other.plate_number

    def __lt__(self, other: "Car") -> bool:
        if not isinstance(other, Car):
            return NotImplemented
        return self.milage < other.milage

# Input
if __name__ == "__main__":
# Create 3 cars
    car1 = Car("ABC-123", "Model A", battery_level=80, milage=120000, status="Available")
    car2 = Car("XYZ-566", "Model B", battery_level=60, milage=10000, status="Available")
    car3 = Car("LMN-056", "Model C", battery_level=40, milage=90000, status="Available")

    car1.drive(400)
    print(car1)
    car1.drive(400)
    print(car1)
    car1.drive(400)
    print(car1)
    

# Sorting by milage
    sorted_cars = sorted([car1, car2, car3])
    for car in sorted_cars:
        pass
# Compare cars
    car2_compar = Car("ABC-123", "Model A" , milage=120000)
    print("car1 == car2_compar:", car1 == car2_compar)

#FOR CHECK __STR___
    print("car1:", car1)


class Driver:
    def __init__(self, name: str, experience_level: int, assigined_cars=None):
        self.name = name
        self.experience_level = experience_level if 1 <= experience_level <= 10 else None
        self.assigined_cars = assigined_cars if assigined_cars else []

    def assigin_car(self, *cars):
        for car in cars:
            if not isinstance(car, Car):
                return NotImplemented
            self.assigined_cars.append(car)

    def __repr__(self: str):
        if self.assigined_cars:
            cars = ", ".join(car.model for car in self.assigined_cars)
            return f"{self.name} - experience: {self.experience_level}, cars: {cars}"
        else:
            return f"{self.name} - experience: {self.experience_level}, cars: owns no cars!"
        
    def __bool__(self) -> bool:
        return bool(self.assigined_cars)
    

driver1 = Driver("Peter", 11)

if driver1:
    print("Yes!")
else:
    print("No!")

print(repr(driver1))

driver1.assigin_car(car1, car2)

print(repr(driver1))

class Customer:
    def __init__(self,name:str,credit_balance:int,trips:list):
        self.name=name
        self.credit_balance=credit_balance
        self.trips=trips
        
    
    def __iadd__(self,amount:int):
        if amount>0:
            return self.credit_balance + amount
    
    def __isub__(self,amount:int):
        if amount>0:
            return self.credit_balance - amount
    
    def __len__(self):
        return len(self.trips)
    
    def __str__(self) -> str:
        return f"name={self.name} {self.credit_balance} {self.trips}"
    def __repr__(self) -> str:
        return f"name={self.name} {self.credit_balance} {self.trips}"
    
    

customer1=Customer("amir",100,["thran","londan"])
customer1.credit_balance+=100
print(customer1.credit_balance)

customer1.credit_balance-=50
print(customer1.credit_balance)

print(len(customer1))
print(customer1)

class Trip:
    trip_id = 1000
    def __init__(self, driver, customer, distance_km: float, price_per_km:float):
        self.trip_id = Trip.trip_id 
        Trip.trip_id += 1
        self.driver = driver
        self.customer = customer
        self.distance_km = distance_km
        self.price_per_km = price_per_km
    
    def calculate_cost(self):
        return self.distance_km * self.price_per_km
        
    
    def __str__(self):
        return f"Trip #{self.trip_id}: {self.driver.name} _ {self.customer.name}({self.distance_km}km, ${self.calculate_cost()})"
    
    def __call__(self):
        return self.calculate_cost()
    
customer1=Customer("amir",100,[])
customer1.credit_balance+=100
print(customer1.credit_balance)

customer1.credit_balance-=50
print(customer1.credit_balance)

print(len(customer1))
print(customer1)

trip1 = Trip(driver1, customer1, 12.0, 2.5)
print(trip1)

customer1.trips.append(trip1)
print(customer1)
print(trip1())


class Fleet:
    def __init__(self):
        self.cars = []
        self.drivers = []

    def __len__(self) -> int:
        return len(self.cars)

    def __getitem__(self, index: int) -> Car:
        return self.cars[index]

    def __iter__(self):
        return iter(self.cars)

    def add_car(self, car: Car):
        self.cars.append(car)

    def add_driver(self, driver: Driver):
        self.drivers.append(driver)

    def find_available_cars(self):
        for car in self.cars:
            if car.status == "available":
                return car
        return None
# Testing Class Fleet
if __name__ == "__main__":
    fleet = Fleet()



    fleet.add_car(car1)
    fleet.add_car(car2)
    fleet.add_car(car3)

print(f"Total car in fleet:")
for car in fleet:
    print(car)

    print(f"Accessing 2nd car in fleet:")
    print(fleet[1])

    print(f"Finding 1st car in fleet:")
    avialable_car =fleet.find_available_cars()
    if avialable_car:
        print(f"found {avialable_car}")
    else:
        print("No available cars")


import pickle

class SystemDatabase:
    def __init__(self,filename):
        self.filename=filename

    def save_to_file(self,data):
        with open(self.filename,"wb")as file:
            pickle.dump(data,file)

    def load_to_file(self):
        try:
            with open(self.filename,"rb")as file:
                
                print(pickle.load(file))
            
        except FileNotFoundError:
            return 'not found file'

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        return self
    
if __name__=='__main__':

    customers = [
        Customer("Reza", 50,['thran']),
        Customer("Ali",100,[]),
        Customer("Sara", 75,['london'])
    ]
    
    

    db = SystemDatabase("customer.pkl")
    db.save_to_file(customers)
    print("saved to customer.pkl")

    loaded_customers = db.load_to_file()
    print("\n loaded Customers:")
for customer in customers:
    print(customer)
    
    with open("customer2.pkl", "wb") as f:
        pickle.dump(customers, f)
        print("saved")

    with open("customer2.pkl", "rb") as f:
        loaded_customers = pickle.load(f)
        print("\nloaded customers")
        for customer in loaded_customers:
            print(customer)
    
class SmartCar(Car):
    def __init__(self, plate_number: str, model: str, battery_level: int = 100, milage: float = 0.0, status: str = "available"):
        super().__init__(plate_number, model, battery_level, milage, status)
        self.ai_status="OK"

    def drive(self, km:float):
        if self.battery_level < 10:
            print(f"Battery level below 10%.")
            self.charge(100-self.battery_level)
            print(f"Battery level: {self.battery_level}%")
        super().drive(km)

        if self.milage > 100000:
            self.status = "Maintenance needed"
            self.ai_status ="Maintenance require"

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info} [AI Status: {self.ai_status}]"

#Usage
if __name__ == "__main__":
    smart_car = SmartCar("XYZ-566", "Model B", battery_level=5, milage=1000000)
    print(smart_car)

    try:
        smart_car.drive(600.0)
    except ValueError as e:
        print("Error:",e)
    print("\nafter driving")
    print(smart_car)

class SmartCar(Car):
    def __init__(self, plate_number: str, model: str, battery_level: int = 100, milage: float = 0.0, status: str = "available"):
        super().__init__(plate_number, model, battery_level, milage, status)
        self.ai_status="OK"

    def drive(self, km:float):
        if self.battery_level < 10:
            print(f"Battery level below 10%.")
            self.charge(100-self.battery_level)
            print(f"Battery level: {self.battery_level}%")
        super().drive(km)

        if self.milage > 100000:
            self.status = "Maintenance needed"
            self.ai_status ="Maintenance require"

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info} [AI Status: {self.ai_status}]"

    smart_car = SmartCar("XYZ-566", "Model B", battery_level=5, milage=1000000)
    print(smart_car)

try:
    smart_car.drive(600.0)
except ValueError as e:
    print("Error:",e)
print("\nafter driving")
print(smart_car)  


#########Expansion
# class Customer:
#     def __init__(self, name, credit_balance=0):
#         self.name = name
#         self.credit_balance = credit_balance
#         self.trip_history = TripHistory()

#     def __repr__(self):
#         return f"Customer(name='{self.name}', credit_balance={self.credit_balance})"

# class Trip:
#     def __init__(self, trip_id, origin, destination, distance, price_per_km):
#         self.trip_id = trip_id
#         self.origin = origin
#         self.destination = destination
#         self.distance = distance
#         self.price_per_km = price_per_km

#     def calculate_cost(self):
#         return self.price_per_km * self.distance

#     def __repr__(self):
#         return f"Trip ({self.trip_id}, {self.origin}, {self.destination}, {self.distance}, {self.price_per_km})"

# class TripHistory:
#     def __init__(self):
#         self.trips = []
#     def add_trip(self, trip):
#         self.trips.append(trip)
#     def __getitem__(self, index):
#         return self.trips[index]
#     def __repr__(self):
#         return f"TripHistory(trips={self.trips})"

# class Bill:
#     def __init__(self, customers, amount):
#         self.customers = customers
#         self.amount = amount
#     def __add__(self, other):
#         # if self.customers.name != other.customers.name:
#         #     raise ValueError("Can't add up the same customer")
#         return Bill(self.customers, self.amount + other.amount)

#     def __repr__(self):
#         return f"Bill(customers={self.customers.name}, amount={self.amount})"




# def simulate_trip(trip_id ,cutomer, origin, destination, distance, price_per_km):
#     trip = Trip(trip_id, origin, destination, distance, price_per_km)
#     cost = trip.calculate_cost()
#     cutomer.trip_history.add_trip(trip)
#     customer.credit_balance -= cost
#     print(f"trip completed: {trip} --- remaining balance: {customer.credit_balance}")




# if __name__ == "__main__":
#     customer1 = Customer("Reza", credit_balance=50)
#     customer2 = Customer("Reza", credit_balance=75)
#     customer3 = Customer("Ali", credit_balance=100)
#     threads = [
#         threading.Thread(target=simulate_trip, args=("T001", customer1, "A", "B", 10, 2.5)),
#         threading.Thread(target=simulate_trip, args=("T002", customer1, "A", "B", 5, 3.0)),
#         threading.Thread(target=simulate_trip, args=("T002", customer3, "C", "B", 10, 5.0)),
#     ]

#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()

#     print(f"{customer1.name} trip history" , customer1.trip_history[0:1])
#     print(f"{customer3.name} trip history", customer3.trip_history[:])

#     #mrging bills
#     bill1 = Bill(customer1, 10)
#     bill2 = Bill(customer1, 5)
#     merged_bill = bill1 + bill2
#     print(f"Merged bill: {merged_bill}")

class TripWithLogging(Trip):

    def log_action(status):
        def inner_log(func):
            def wrapper(self):
                if status=="trip_start":
                    with open("trips.log","a")as f:
                        start=datetime.now()
                        data=f"#{self.trip_id} started in {start}\n"
                        f.write(data)
                        return func(self)
                elif status=="trip_end":
                    with open('trips.log','a')as f:
                        end=datetime.now()
                        data=f"#{self.trip_id} end in {end}\n"
                        f.write(data)
                        return func(self)
                else:
                    return func(self)
            return wrapper
        return inner_log

    @log_action("trip_start")
    def start_trip(self):
        print(f"trip #{self.trip_id} started.")

    @log_action("trip_end")
    def end_trip(self):
        print(f"trip #{self.trip_id} ended")

trip1 = TripWithLogging("Ali", "Reza", 15.0, 2.5)
trip1.start_trip()
trip1.end_trip()

trip2 = TripWithLogging("Amin", "Sobhan", 12.0, 3)
trip2.start_trip()
trip2.end_trip()
