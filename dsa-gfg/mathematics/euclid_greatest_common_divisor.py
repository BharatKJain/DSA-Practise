def optimized_division_approach(a: int, b: int):
    if b == 0:
        return a
    else:
        return optimized_division_approach(b, a % b)


def subtraction_approach(a: int, b: int):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def brute_force_approach(a: int, b: int):
    res = min(a, b)
    while res > 0:
        if a % res == 0 and b % res == 0:
            break
        res -= 1
    return res


if __name__ == "__main__":
    print(f"Brute Force Approach:{brute_force_approach(129,15000000)}")
    print(f"Optimized Approach:{optimized_division_approach(129,15000000)}")
