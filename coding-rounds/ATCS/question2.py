def maxmarks(input1,input2):
    # main_set=list(set(input2)).sort()
    # main_list=[]    
    # for element in main_set:

    # print(main_list)
    # return sum(main_list)
    main_set=set()
    main_list=[]    
    for index in range(input1):
        ele=input2[index]
        if ele in main_set:
            main_list.append(main_list[index-1]+1)
        else:
            main_list.append(input2[index])
            main_set.add(input2[index])
    print(main_list)
    return sum(main_list)

if __name__ == "__main__":
    input1=5
    input2=[1,4,5,4,5]
    print(maxmarks(input1,input2))