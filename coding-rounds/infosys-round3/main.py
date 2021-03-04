import io,os

if __name__=="__main__":
    array=[]
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n=int(input().decode())
    m=int(input().decode())
    k=int(input().decode())
    main_sum=0
    # temp_sum=0
    for row in range(n):
        temp_array=[int(element) for element in input().split()]
        temp_array.sort(reverse=True)
        size_check=0
        for index in range(m):
            if size_check>=(m//2):
                break
            temp_sum=main_sum+temp_array[index]
            if temp_sum%k==0 and temp_array[index]>0:
                main_sum+=temp_array[index]
                size_check+=1
    print(main_sum)