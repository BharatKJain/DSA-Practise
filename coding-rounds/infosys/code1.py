
def countOccurrances(n, d): 
	count = 0
	while (n > 0): 

		if(n % 10 == d): 
			count = count + 1

		n = n // 10
	return count 

x=int(input())
count=0
count_arr=[]
while x:
    l,r,k,p=[int(element) for element in input().split()]
    # print(l,r,p,k)
    # print(f"l:{l},r:{r}")
    for number in range(l,r+1):
        if countOccurrances(number,k)==p:
            count+=1
    count_arr.append(count)
    x-=1
    count=0
print(*count_arr)
    
