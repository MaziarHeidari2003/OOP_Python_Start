class Jar:
  def __init__(self, capacity=12):
        if capacity < 0 or type(capacity) != int:
             raise ValueError('Invalid capacity')    
        self._capacity = capacity
        self._size = 0

        

  def __str__(self):
       return self._size * '🍪'
      

  def deposit(self, n):
      if n > self.capacity :
          raise ValueError('Eceed Capacity')
      if self.size + n > self.capacity:
          raise ValueError('Exceed Capacity')
      self._size += n
  


  def withdraw(self, n):
      if n > self.size:
          raise ValueError('There arent enough cookies in the jar')
      self._size -= n



  
  @property
  def capacity(self):
      return self._capacity



  @property
  def size(self):
      return self._size

jar  = Jar()
jar.deposit(11)
jar.withdraw(10)
print(jar)  