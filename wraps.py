from functools import cache, partial, wraps

def with_greeting(func):
  """
  Wraps is an optional mechanism to make using decorators
  easier and reduce unexpected behavior.
  """
  @wraps(func)
  def wrapper(*args, **kwargs):
    print('Hello world')
    return func(*args, **kwargs)
  
  return wrapper

@with_greeting
def add(x, y):
  """Adds two numbers together"""
  print(x + y)

if __name__ == '__main__':
    add(2, 5)
    add2and5 = partial(add, 2, 5)
    add2and5()