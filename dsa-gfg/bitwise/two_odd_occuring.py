def bitwise(x):
    a = x >> 1
    b = x << 1
    return [a , b]

x=int(input("Enter the Number:"))
print(bitwise(x))