def brute_force_solution(n: int):
    if n == 1:
        return False
    for i in range(2, n):
        if not n % i:
            return False
    return True


def brute_force_solution_with_optimization(n: int):
    if n == 1:
        return False
    for i in range(2, n ** 0.5):
        if not n % 1:
            return False
        return True


def optimized_solution(n: int):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, n + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
