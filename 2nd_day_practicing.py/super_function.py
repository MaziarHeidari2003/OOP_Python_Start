class Regtangle:
  def __init__(self,width,length):
    self.width = width
    self.length = length

class Square(Regtangle):
  def __init__(self,width,length):
    super(). __init__(width,length)
    

  def area(self):
    return self.width*self.length  

class Cube(Regtangle):
  def __init__(self,width,length,height):
    super(). __init__(width,length)
    self.height = height
  def volume(self):
    return self.width*self.length*self.height    

square = Square(3,3)
cube = Cube(3,3,3)
print(square.area())
print(cube.volume())
  