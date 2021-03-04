"""
Given an array of n numbers that has values in range [1,....n]. Every no appears exactly once.Hence one no. is missing.
I/P: arr[]=[1,4,3]
O/P: 2

SOlution : XOR all values
"""
def fetch(array:list)->int:
    res=0
    for element in range(1,max(array)+1):
        res^=element
    for element in array:
        res^=element
    return res
if __name__=="__main__":
    print("result: ",fetch([1,4,3]))