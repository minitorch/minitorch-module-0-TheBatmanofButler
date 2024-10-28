"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(a: float, b: float) -> float:
    return a * b

def id(a: float) -> float:
    return a

def add(a: float, b: float) -> float:
    return a + b

def neg(a: float) -> float:
    return -a

def lt(a: float, b: float) -> float:
    return a < b

def eq(a: float, b: float) -> float:
    return a == b

def max(a: float, b: float) -> float:
    return a if a > b else b

def is_close(a: float, b: float) -> bool:
    if abs(a - b) <= abs(a) / 100 or abs(a - b) <= abs(b) / 100:
        return True

    return False

def sigmoid(a: float) -> float:
    if a > 0:
        return 1 / (1 + math.exp(-a))
    else:
        e_a = math.exp(a)
        return e_a / (1 + e_a)

def relu(a: float) -> float:
    return (a + abs(a)) / 2

def log(a: float) -> float:
    return math.log(a)

def exp(a: float) -> float:
    return math.exp(a)

def inv(a: float) -> float:
    return 1 / a

def log_back(a: float, b: float) -> float:
    return inv(a) * b

def inv_back(a: float, b: float) -> float:
    return -b / a ** 2

def relu_back(a: float, b: float) -> float:
    return b if a > 0 else 0

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

def map(iterable: Iterable, func: Callable) -> Iterable:
    return [func(a) for a in iterable]

def zipWith(iterableA: Iterable, iterableB: Iterable, func: Callable) -> Iterable:
    if len(iterableA) != len(iterableB):
        raise ValueError("Iterables must be the same length.")

    return [func(iterableA[index], iterableB[index]) for index, _ in enumerate(iterableA)]

def reduce(iterable: Iterable, func: Callable) -> float:
    if len(iterable) < 1:
        return 0

    result = iterable[0]
    for a in iterable[1:]:
        result = func(a, result)
    
    return result

def negList(iterable: Iterable) -> Iterable:
    return map(iterable, neg)

def addLists(iterableA: Iterable, iterableB: Iterable) -> Iterable:
    return zipWith(iterableA, iterableB, add)

def sum(iterable: Iterable) -> float:
    return reduce(iterable, add)

def prod(iterable: Iterable) -> float:
    return reduce(iterable, mul)
