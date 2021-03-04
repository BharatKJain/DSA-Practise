def naive_solution_count_set_bits(n: int) -> int:
    res = 0
    while n > 0:
        if n % 2 == 1:
            res += 1
        n //= 2
    return res


def brian_kerningam_method(n: int) -> int:
    res = 0
    while n > 0:
        n = n & (n - 1)
        res += 1
    return res

# table = [0]*256
# def look_up_table_method(n:int):
#     def initialize():
#         global table
#         table[0] = 0
#         table = [(element&1)+table[element//2] for element in range(1,256)]
#     def count(n:int):
#         global table
#         res=table[n&0xff]
#         n=n>>8
#         res=res+table[n&0xff]
#         n=n>>8
#         res=res+table[n&0xff]
#         n=n>>8
#         res=res+table[n&0xff]
#         return res
#     initialize()
#     return count(n)


if __name__ == "__main__":
    print("Naive: ", naive_solution_count_set_bits(1023))
    print("Brian Kerningam's Method: ", brian_kerningam_method(1023))
    # print("Look-Up-Table-Method: ",look_up_table_method(1365))
