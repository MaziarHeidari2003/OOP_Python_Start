class Student:
  def __init__(self,name,house) :
    self.name = name
    self.house = house 

  @classmethod
  def get(cls):
    name = input('Name: ')
    house = input('House: ')
    return cls(name,house)

@property
def house(self):
  return self._house  

@house.setter
def house(self,house):
  if house not in ['Griffindor','Hufflepuf','Ravenclaw','Slytherin'] :
    raise ValueError('Invalid house')
  self._house = house   
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self,name):
    if not name:
      raise ValueError('Missing name')
    self._name = name
    



  def __str__(self):
    return f'{self.name} from {self.house}'
  
  def charm(self):
    match self.patronus:
      case 'Stag':
        return 1
      case 'Otter':
        return 2
      case 'Jack Rissel terrior':
        return 3
      case _:
        return 0



def main():
  student = Student.get()
  print(student.house)


if __name__ == '__main__' :
  main()
