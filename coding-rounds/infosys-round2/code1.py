
main_data_array = []

def findCombinationsUtil(arr, index, num,
                              reducedNum):
    global main_data_array
    temp_arr = []

    if (reducedNum < 0):
        return

    if (reducedNum == 0): 
  
        for i in range(index): 
            temp_arr.append(arr[i])
        main_data_array.append(temp_arr)
        temp_arr = []
        return; 
  

    prev = 1 if(index == 0) else arr[index - 1]; 
    for k in range(prev, num + 1): 
        arr[index] = k; 
        findCombinationsUtil(arr, index + 1, num,  
                                 reducedNum - k);
def findCombinations(n): 
	arr = [0] * n; 
	findCombinationsUtil(arr, 0, n-1, n); 

if __name__ == "__main__":
    testcase = int(input())
    while testcase:
        main_input=[int(element) for element in input().split()]
        n = main_input[0]
        m = main_input[1]
        findCombinations(n)
        main_sum=0 
        for array in main_data_array:
            if len(array) == m:
                main_sum=((main_sum+sum((element**2 for element in array)))%(10**9+7))
        print(main_sum)
        main_data_array = []
        testcase-=1