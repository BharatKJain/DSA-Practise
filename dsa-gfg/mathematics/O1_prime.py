from math import floor
from decimal import *

getcontext().prec = 30
MAIN_NUMBER = 2.920050977316
DECIMAL_PORTION = 0.920050977316

# f(n+1) = floor( f(n) ) * ( f(n) - floor(f(n)) + 1 )


def math_function(fn: int):
    return Decimal(floor(fn) * (fn - floor(fn) + 1))


def producer(n: int):
    for index in range(n):
        if index == 0:
            carry = MAIN_NUMBER
            print(floor(MAIN_NUMBER))
        carry = math_function(carry)
        print(carry)
        print(floor(carry))


if __name__ == "__main__":
    range_input = int(input())
    producer(range_input)
