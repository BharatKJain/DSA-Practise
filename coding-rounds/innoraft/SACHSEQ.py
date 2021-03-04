if __name__ == "__main__":
t=int(input())
while t>0:
    n,k=map(int,input().split(" "))
    arr=[int(element) for element in input().split(" ")]
    mod =[] 
    for i in range(k + 1): 
        mod.append(0)
    cumSum = 0
    for i in range(n): 
        cumSum = cumSum + arr[i] 
        mod[((cumSum % k)+k)% k]= mod[((cumSum % k)+k)% k] + 1
    result = 0  
    for i in range(k): 
        if (mod[i] > 1): 
            result = result + (mod[i]*(mod[i]-1))//2
    result = result + mod[0]
    print(result)
    t-=1