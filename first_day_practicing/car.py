class Car:
  wheels = 4
  def __init__(self,model,make,year,color):
    self.model = model
    self.make = make
    self.year = year
    self.color = color
    
  def drive(self):
    print("This car is driving")
  def stop(self):  
    print("This car is stopped")  