"""
Important link:
https://www.geeksforgeeks.org/python-itertools/
"""

from itertools import combinations, permutations, combinations_with_replacement, accumulate
from operator import mul

#########################################################################################

# print("All the permutations of the given list is:")
# print(list(permutations([1, 'geeks'], 2)))
# print("All the permutations of the given string is:")
# print(list(permutations('ABCDEFG',2)))
# print("All the permutations of the given container is:")
# print(list(permutations(range(6), 2)))


# print ("All the combination of list in sorted order(without replacement) is:")
# print(list(combinations(['A', 2], 2)))
# print ("All the combination of string in sorted order(without replacement) is:")
# print(list(combinations('ABCDEF', 3)))
# print ("All the combination of list in sorted order(without replacement) is:")
# print(list(combinations(range(6), 2)))


# print ("All the combination of string in sorted order(with replacement) is:")
# print(list(combinations_with_replacement("ABCDEF", 3)))
# print ("All the combination of list in sorted order(with replacement) is:")
# print(list(combinations_with_replacement([1, 2], 2)))
# print ("All the combination of container in sorted order(with replacement) is:")
# print(list(combinations_with_replacement(range(6), 2)))


# # initializing list 1
# li1 = [1, 4, 5, 7]

# # using accumulate()
# # prints the successive summation of elements
# print("The sum after each iteration is : ", end="")
# print(list(accumulate(li1)))

# # using accumulate()
# # prints the successive multiplication of elements
# print("The product after each iteration is : ", end="")
# print(list(accumulate(li1, mul)))


############################################################################################

# print all combination of substring in string:
string = "CHECKING"
print([string[element[0]:element[1]]
       for element in list(combinations(range(len(string)+1), 2))])
