def announce(f):
  def wrapper():
    print('About to run the function')
    f()
    print('All done')
  return wrapper

@announce
def hello():
  print('Hello world')

hello()