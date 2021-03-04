n=int(input())
array=[int(element) for element in raw_input().split(" ")]
sumOfNumbers=0
for index in range(0,n,2):
    sumOfNumbers+=array[index]
print(sumOfNumbers)
