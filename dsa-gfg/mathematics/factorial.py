# iterative
def iter_factorial(num: int) -> int:
    """
    Time complexity: O(n)
    """
    if num < 0:
        return -1
    if num in [0, 1]:
        return 1
    result = 1
    for index in range(2, num + 1):
        result *= index
    return result


# recursive
def recur_factorial(num: int) -> int:
    """
    Time complexity: O(n)
    """
    if num < 0:
        return -1
    if num in [0, 1]:
        return 1
    return num * recur_factorial(num - 1)


if __name__ == "__main__":
    print(f"Recursively: {recur_factorial(20)}")
    print(f"Iteratively: {iter_factorial(20)}")
