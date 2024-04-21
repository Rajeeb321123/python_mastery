## python OOP

class Car:
    # variable
    # default is 4. but can be changed for individual objects
    wheels = 4 # all the object created will have this 

    #Constructor , # self means this
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def drive(self):
        print(f"{self.make} {self.model} is driving")
    
    def stop(self):
        print("Car is stopped")


car_1 = Car("Tesla","model_3","2023")
car_2 = Car("CyberTruck","model_1","2022")

print(car_1.make)
car_1.drive()
print(car_1.wheels)
print(Car.wheels)
car_1.wheels  = 3
print(car_1.wheels)
print(car_2.wheels)

car_1.make="Tyota"
print(car_1.make)
