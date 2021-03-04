if __name__ == "__main__":
    inputString=list(input())
    countChar=0
    mainDict={}
    for element in inputString:
        if element in mainDict:
            mainDict[element]+=1
        else:
            mainDict[element]=1
    for k,v in mainDict.items():
        if v==1:
            countChar+=1
    print(countChar)
    