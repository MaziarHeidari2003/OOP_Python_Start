class Animal:
    alive = True
    def eat(self):
      print("This animal is eating")
    def sleep(self):
      print("This animal is sleeoing")

class Rabbit(Animal):
    def run(self):
      print("Rabbit is running")

class Hawk(Animal):
    def fly(self):
      print("The hawk is flying")
class Fish(Animal):
    def swim():
      print("The fish is swimming")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()
rabbit.run()

