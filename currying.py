import functools
from typing import Callable

# Callable[[float, float], float]
def add(a: float, b: float) -> float:
  print(f'get args: {a=} {b=}')
  return a + b


def make_adder(a: float) -> Callable[[float], float]:
    return lambda b: add(a, b)

add_5 = make_adder(5)

add_6 = functools.partial(add, 6)

add_7 = functools.partial(add, b=7)