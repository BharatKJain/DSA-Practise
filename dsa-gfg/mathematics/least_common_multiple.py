def brute_force_approach(a: int, b: int):
    res = max(a, b)
    while True:
        if res % a == 0 and res % b == 0:
            return res
        res += 1
    return res


def gcd(a: int, b: int):
    if b == 0:
        return a
    return gcd(b, a % b)


def optimized_approach(a: int, b: int):
    return (a * b) / gcd(a, b)


if __name__ == "__main__":
    print()
    print()
