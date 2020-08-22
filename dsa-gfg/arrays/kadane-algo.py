# ideal algo:
# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
# from sys import maxint


# def maxSubArraySum(a, size):

#     max_so_far = -maxint - 1
#     max_ending_here = 0

#     for i in range(0, size):
#         max_ending_here = max_ending_here + a[i]
#         if (max_so_far < max_ending_here):
#             max_so_far = max_ending_here

#         if max_ending_here < 0:
#             max_ending_here = 0
#     return max_so_far


# # Driver function to check the above function
# a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
# print "Maximum contiguous sum is", maxSubArraySum(a, len(a))

# This code is contributed by _Devesh Agrawal_


# mycode:
def algo(l:list) -> int:
    flag=0
    max_sum=0
    consecutive_sum=0
    array=[]
    max_array=[]
    for element in l:
        print(element)
        print(f"consecutive:{consecutive_sum}")
        consecutive_sum+=element
        array.append(element)
        if max_sum < consecutive_sum:
            max_sum=consecutive_sum
            max_array=array.copy()
        if consecutive_sum < 0:
            consecutive_sum=0
            array=[]
    return {"sum":max_sum,"array":max_array}

# a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
a=[-2, -3, 4, -1, -2, 1, 5, -3,-5]
print(algo(a))