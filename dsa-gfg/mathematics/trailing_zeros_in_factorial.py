from factorial import iter_factorial
"""
Naive approach: fetch factorial and count zeros
"""
def trailing_zeros(num:int)->int:
    count=0
    factorial=iter_factorial(num)
    while factorial>0:
        right_digit=factorial%10
        if right_digit!=0:
            break
        count+=1
        factorial=factorial//10
    return count
"""
Optimized approach: count the number of 5x2 pairs, 5's are always going
to be less than 2's thus we count the no of 5's
"""
def optimized_trailing_zeros(num:int)->int:
    index=5
    count_of_zeros=0
    while index<num:
        count_of_zeros+=(num//index)
        index*=5

if __name__ == "__main__":
    print(trailing_zeros(10))
