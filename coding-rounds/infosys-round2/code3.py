def findClosest(arr, n, target): 
  
    # Corner cases 
    if (target <= arr[0]): 
        return arr[0] 
    if (target >= arr[n - 1]): 
        return arr[n - 1] 
 
    i = 0; j = n; mid = 0
    while (i < j):  
        mid = (i + j) // 2
  
        if (arr[mid] == target): 
            return arr[mid] 
        if (target < arr[mid]) : 

            if (mid > 0 and target > arr[mid - 1]): 
                return getClosest(arr[mid - 1], arr[mid], target) 
            j = mid 

        else : 
            if (mid < n - 1 and target < arr[mid + 1]): 
                return getClosest(arr[mid], arr[mid + 1], target) 

            i = mid + 1
    return arr[mid] 
def segregator_and_finalizer(input_data:list,K:int):
    even_list=[]
    odd_list=[]
    for element in input_data:
        if element%2==0:
            even_list.append(element)
        else:
            odd_list.append(element)
    odd_list.sort()
    even_list.sort()
    odd_map = dict((odd_list[index],index)for index in range(len(odd_list)))
    even_map = dict((even_list[index],index)for index in range(len(even_list)))
    left_side_sum = 0
    right_side_sum = (odd_list[-1]+even_list[-1])%K
    for index in range(len(odd_list)):
        diff = K - odd_list[index]
        if diff < 0:
            break
        closest_number = findClosest(even_list,len(even_list),diff)
        if closest_number == diff:
            temp_index = even_map[closest_number]
            closest_number = even_list[temp_index-1]
        if (closest_number+odd_list[index])%K > left_side_sum:
            left_side_sum = (closest_number+odd_list[index])%K
    if left_side_sum > right_side_sum:
        return left_side_sum
    return right_side_sum

if __name__ == "__main__":
    testcase = int(input())
    while testcase:
        number_of_elements = int(input())
        list_of_elements =[int(element) for element in input().split()]
        k = int(input())
        return_data = segregator_and_finalizer(list_of_elements,k)
        print(return_data)
        testcase-=1