# class DateTime():
#     def __init__(date,month,year):
#         if type(date)==int:
#             raise TypeError("Error wih date")
#         if date not in range(1,32):
#             raise Exception("Incorrect Date")
#         if month not in range(1,13):
#             raise Exception("Incorrect Month")
#         if year not in range(1970,2020):
#             raise Exception("Incorrect Year")
#         self.date=date
#         self.month=month
#         self.year=year
#         print("Correct Date")

# if __name__ =="__main__":

# first_num = 1
# second_num = 2
# n = int(input("N:"))
# for index in range(0,n):
# 	if index == 0:
# 		print(first_num,end=",")
# 	elif index == 1:
# 		print(second_num,end=",")
# 	else:
# 		print(first_num*second_num,end=",")
# 		temp = first_num
# 		first_num = second_num 
# 		second_num = temp*second_num

# sum_of_number=20

# for index in range(sum_of_number,0,-1):
#     print(index)

def reverseStr(s):
    i=0
    j=len(s)-1
    while i < j:
        s[i]=s[j]
        s[j]=s[i]
        i+=1
        j-=1
    return "".join(s)
s=list(input())
print(reverseStr(s))

# string = "ABCD"
# x=list(string)
# temp = x[3]
# x[3] = x[0]
# x[0] = temp
# new_string = "".join(x)
# print(new_string)
