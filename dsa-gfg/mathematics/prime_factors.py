from check_for_prime import optimized_solution as is_prime


def prime_factors(n: int):
    for i in range(2, n):
        if is_prime(i):
            x = i
            while not n % x:
                print(i)
                x *= i


if __name__ == "__main__":
    # print(is_prime(6))
    prime_factors(12)
