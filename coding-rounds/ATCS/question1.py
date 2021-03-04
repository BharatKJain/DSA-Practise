def find(input1, input2):
    def gcd(a, b): 
        if (a == 0 or b == 0): return 0
        if (a == b): return a
        if (a > b):  
            return gcd(a - b, b) 
                
        return gcd(a, b - a) 
    def coprime(a, b): 
        if ( gcd(a, b) == 1): 
            return True
        else: 
            return False
    for index in range(input2-1):
        if coprime(input1[index],input1[index+1]) and (input1[index]>input1[index+1]):
            return index


if __name__ == "__main__":
    input1=[4,1,3,2]
    input2=4
    print(find(input1,input2))