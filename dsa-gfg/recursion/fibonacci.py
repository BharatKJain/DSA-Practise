def fibo(a):
    if a <= 0:
        return 1
    return fibo(a - 1) + fibo(a - 2)


if __name__ == "__main__":
    n = int(input())
    for index in range(n):
        print(fibo(index))