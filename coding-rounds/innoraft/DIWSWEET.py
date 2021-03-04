if __name__ == "__main__":
    t=int(input())
    while t>0:
        n=int(input())
        array=[int(element) for element in input().split(" ")]
        main_set=dict()
        min_cost=-1
        for index in range(len(array)):
            elem=array[index]
            if elem in main_set:
                main_set[elem]+=1
            else:
                main_set[elem]=1
        for key,value in main_set.items():
            if value==1 and (min_cost<key or min_cost==-1):
                min_cost=key
        print(min_cost)
        t-=1