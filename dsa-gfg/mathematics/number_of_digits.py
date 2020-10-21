from math import log10,floor
def count_digits_logarithmic(n:int)->int:
    """
    Time complexity: O(1)
    """
    return floor(log10(n)+1)
def count_digits_iterative(n:int)->int:
    """
    Time complexity: O(n)
    """
    count=0
    while n!=0:
        count+=1
        n=n//10
    return count

def count_digits_recursion(n:int)->int:
    """
    Time complexity: O(n)
    """
    if n==0:
        return 0
    return 1+count_digits_recursion(n//10)

if __name__ == "__main__":
    input_number=int(input())
    print(count_digits_recursion(input_number))
    print(count_digits_logarithmic(input_number))
    print(count_digits_iterative(input_number))