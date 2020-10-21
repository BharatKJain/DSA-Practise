def lowerBetweenNumbers(a,b):
    if a<b:
        return a
    else:
        return b
def higherBetweenNumbers(a,b):
    if a>b:
        return a
    else:
        return b
def lowestFactors(number):
    for index in range(2,number+1):
        if number%index==0:
            return [index,number//index]
if __name__ == "__main__":
    number=15
    listOfNumbers=[2,4,6]
    lowFactors=lowestFactors(15)
    print(lowFactors)
    count=0
    for element_x in listOfNumbers:
        if element_x<=lowerBetweenNumbers(lowFactors[0],lowFactors[1]):
            for element_y in listOfNumbers:
                if element_y <= higherBetweenNumbers(lowFactors[0],lowFactors[1]):
                    count+=1
                else:
                    break
    print(count)
