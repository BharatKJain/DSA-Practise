"""
    Program to find the odd occuring number(XOR approach)
"""
def naive(array:list)->None:
    count=0
    for index_i in range(n):
        count=0
        for index_j in range(n):
            if array[index_i]==array[index_j]:
                count+=1
        if count%2!=0:
            print(array[index_i])

def optimized(array:list)->None:
    res=0
    for index_i in range(n):
        res=res^array[index_i]
    return res

if __name__=="__main__":
    print("Naive Approach: ", naive([4,3,4,4,4,5,5]))
    print("Optimzied: ",optimized([4,3,4,4,4,5,5]))
    