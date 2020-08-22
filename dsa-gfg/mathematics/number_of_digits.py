def print_digits(number):
    construct_list=[]
    while number:
        construct_list.append(number%10)
        number//=10
    return construct_list
if __name__ == "__main__":
    input_number=input()
    data=[int(element) for element in list(input_number)]
    print(data)
    print(print_digits(int(input_number)))