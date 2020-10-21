# def fetchNthNumber(n,x):
#     # init_number=2
#     sequence=[element for element in range(x-1,-1,-1)]
#     # print(sequence)
#     # sequence=[4,3,2,1,0]
#     if n==1:
#         print(x)
#     else:
#         increment=n//20
#         index=(n//2-1)%x
#         index=(index+increment)%x
#         if n%2==0:
#             print(n*x+sequence[index])
#         else:
#             print(n*x+sequence[index])
def fetchNthNumber(n):
    # init_number=2
    sequence=[4,3,2,1,0]
    if n==1:
        return(5)
    else:
        increment=n//20
        index=(n//2-1)%5
        index=(index+increment)%5
        if n%2==0:
            return(n*5+sequence[index])
        else:
            return(n*5+sequence[index])
def main():
    # for index in range(1,10):
    #     print(fetchNthNumber(index))
    number=int(input())
    number2=int(input())
    if number%5==0:
        index=(number//5)
    else:
        index=(number//5)+1
    print(fetchNthNumber(index+number2-1))

if __name__ == "__main__":
    main()