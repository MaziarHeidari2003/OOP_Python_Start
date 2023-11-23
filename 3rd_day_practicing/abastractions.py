from abc import ABC, abstractmethod

class Vehicle(ABC):
  @abstractmethod
  def go(self):
    pass
  @abstractmethod
  def stop(self):
    pass

class Car(Vehicle):
  def go(self):
    print("The car is going")  
  def stop(self):
    print("The car is stopping")


class Bycicle(Vehicle):
  def go(self):
    print("The bike is going")
  def stop(self):
    print("The bike is stopping")
  
 

car = Car()
bycicle = Bycicle()
car.go()
bycicle.go()

