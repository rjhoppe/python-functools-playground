from functools import cache, lru_cache
"""
The below fib function works, but is inefficient due to
the fact that it repeats calculations that have already
been performed instead of remembering them.
"""
# def fib(n):
#   if n <= 1:
#     return n
#   return fib(n-1) + fib(n-2)


"""
Now previous calculations are cached and remembered
by the function. This substantially improves performance.
""" 
# @cache
# def fib(n):
#   if n <= 1:
#     return n
#   return fib(n-1) + fib(n-2)

"""
Another way this can be done is using an LRU (least recently used) cachce. This
allows you to set a size for your cache that the calculation remembers. This can
decrease memory usage / allocation at runtime.
"""
@lru_cache(maxsize=5)
def fib(n):
  if n <= 1:
    return n
  return fib(n-1) + fib(n-2)


def main():
  for i in range(400):
    print(1, fib(1))
  print("done")

if __name__ == '__main__':
  main()


