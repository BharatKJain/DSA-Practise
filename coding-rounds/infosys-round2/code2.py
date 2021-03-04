number_of_nodes=int(input())
flag = 0
loop_count=1
while loop_count < number_of_nodes:
    try:
        raw_inp = input()
    except:
        break
    loop_count+=1
raw_inp = input()
main_values = [int(element) for element in raw_inp.split()]
raw_inp = int(input())
K = int(raw_inp)
max_sum = sum([value^K if value^K > value else value for value in main_values])
print(max_sum)