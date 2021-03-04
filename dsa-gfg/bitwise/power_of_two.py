"""
Program to check if a number is a power of two
"""

def naive(n:int)->bool:
    if not n:
        return False
    while n!=1:
        if n%2!=0:
            return False
        n/=2
    return True

def optimized(n:int)->bool:
    return (n!=0 and (not n&(n-1)))

if __name__=="__main__":
    print("Naive Approach: ",naive(1048576))
    print("Optimized Approach: ",optimized(1048576))