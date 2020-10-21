#For numbers

def is_palindrome(num:int)->bool:
    """
    Time complexity: O(n)
    """
    rev=0
    temp=num
    while num>0:
        rev=rev*10+(num%10)
        num=num//10
    return rev==temp
if __name__ == "__main__":
    print(is_palindrome(353))