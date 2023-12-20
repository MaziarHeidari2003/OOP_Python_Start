class Prey:
  def flee(self):
    print("This animal flees")


class Predator:
  def hunt(self):
    print("This animal is hunting")    

class Fish(Prey,Predator):
  def wake_up(self):
    print("The cute fish wakes up")
    return self
  def swim(self):
    print("The fish is swimming")
    return self
  def danger(self):
    print("High speed of swimming and cought by the police!!!")  
    return self 

fish1 = Fish()
fish2 = Fish()

fish1.flee()
fish1.hunt()
print()
fish2.wake_up()\
     .swim()\
     .danger()