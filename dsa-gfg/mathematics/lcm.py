from time import perf_counter 

def 

def iter_gcd(a: int, b: int) -> int:
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def gcd(a: int, b: int) -> None:
    if b == 0:
        # print(a)
        return a
    return gcd(b, a % b)


def fetch_gcd(a: int, b: int) -> None:
    if iter==True:
        if a == b:
            return a
        elif a > b:
            return iter_gcd(a, b)
        else:
            return iter_gcd(b, a)
    else:
        if a == b:
            return a
        elif a > b:
            return gcd(a, b)
        else:
            return gcd(b, a)


if __name__ == "__main__":
    """
        input:a b
        output: HCF(a,b)
    """
    start_time=perf_counter()
    # brute force
    main_element = 0
    inp = [int(element) for element in input().split(" ")]
    for number in range(1, min(inp)+1):
        if inp[0] % number == 0 and inp[1] % number == 0:
            main_element = number
    print(main_element)
    print(f"Time for brute force: {perf_counter()-start_time}")
    # optimal way:recursion
    ######################
    #   GCD(a,b)=GCD(b,a%b)
    #   GCD(a,0)=a
    #######################
    start_time=perf_counter()
    main_element = 0
    print(fetch_gcd(inp[0], inp[1]))
    print(f"Time for recursion gcd: {perf_counter()-start_time}")
    # optimal way:iteration
    start_time=perf_counter()
    print(iter_gcd(inp[0], inp[1]))
    print(f"Time for iterative gcd: {perf_counter()-start_time}")