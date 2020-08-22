"""
    This code includes 0 in array so please use index+1
"""


def return_sieve(number: int) -> None:
    prime_sieve = [True for _ in range(number+1)]
    pointer = 2
    while pointer*pointer <= number:
        if prime_sieve[pointer] == True:
            for index in range(pointer * 2, number + 1, pointer):
                prime_sieve[index] = False
        pointer += 1
    prime_sieve[0] = False
    prime_sieve[1] = False
    return prime_sieve

def sieve(number: int) -> None:
    prime_sieve = [True for _ in range(number+1)]
    pointer = 2
    while pointer*pointer <= number:
        if prime_sieve[pointer] == True:
            for index in range(pointer * 2, number + 1, pointer):
                prime_sieve[index] = False
        pointer += 1
    prime_sieve[0] = False
    prime_sieve[1] = False
    # To print the prime numbers till limit
    for pointer in range(number+1):
        if prime_sieve[pointer]:
            print(pointer)


def sieve_find_number(number: int, find_number: int) -> bool:
    fetch_sieve=return_sieve(number)

    return fetch_sieve[number-1]

if __name__ == "__main__":
    number = 30
    sieve(number)
    print(sieve_find_number(number,5))