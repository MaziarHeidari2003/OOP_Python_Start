from car import Car 

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Furd","Mustang",2022,"Red")
car_2.stop()
car_1.drive()
car_1.wheels = 2
print(car_2.wheels)
print(car_1.wheels)