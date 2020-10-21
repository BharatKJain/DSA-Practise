from itertools import permutations


def main():
    for element in list(permutations(range(1,11),3)):
        sumOfSet=sum(element)
        if sumOfSet%2==0:
            print(element)
if __name__=="__main__":
    main()
