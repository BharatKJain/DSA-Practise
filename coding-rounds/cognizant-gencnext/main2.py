def main():
    productCount,kValue=[int(element) for element in input().split(" ")]
    inputProductArray=[int(element) for element in input().split(" ")]
    countOfPairs=0
    dictMain={}
    for element in inputProductArray:
        if element in dictMain:
            dictMain[element]+=1
        else:
            dictMain[element]=1
    for element in inputProductArray:
        diff=element-kValue
        if (element-kValue>0) and (element-kValue in inputProductArray):
            countOfPairs+=1
    return countOfPairs

if __name__ == "__main__":
    print(main())


    