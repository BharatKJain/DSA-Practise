def fetchScore(n,data,indexOfElement):
    #case:1--> 5
    for index in range(indexOfElement,n):
        if data[indexOfElement]<data[index]:
            for index2 in range(index,n):
                if data[index2]<data[index]:
                    return 5
    #case:2 --> 10 
    for index in range(indexOfElement,n):
        if data[indexOfElement]<data[index]:
            return 10
    #case:3 --> 15
    return 15

def main():
    n=int(input())
    ratings=[int(element) for element in input().split()]
    count=0
    for element in range(0,n):
        count+=fetchScore(n,ratings,element)
    print(count)

if __name__ == "__main__":
    main()