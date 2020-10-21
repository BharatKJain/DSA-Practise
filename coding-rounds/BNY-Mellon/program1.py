
def main():
    num=int(input("Enter the number: "))
    chunks_of_zeros=0
    chunks_of_ones=0
    previous_result=-1
    flag=0
    for element in range(num):
        n=int(input())
        if previous_result!=n:
            flag=n
            if flag==0:
                chunks_of_zeros+=1
            if flag==1:
                chunks_of_ones+=1
        previous_result=n
    minimum_quant=min([chunks_of_zeros,chunks_of_ones])
    if num==1:
        print(1)
    else:
        print(minimum_quant+1)
        
if __name__ == "__main__":
    main()