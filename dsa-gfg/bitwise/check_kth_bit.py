def check_kth_bit(n: int, k: int) -> bool:
    if not n & (1 << k):
        return True
    else:
        return False


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    print(check_kth_bit(n, k))
