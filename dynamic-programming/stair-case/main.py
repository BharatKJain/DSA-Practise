def fetch_minimum_staircase(steps,steps_to_be_taken,dict_mem):
    if steps_to_be_taken in dict_mem:
        return dict_mem[steps_to_be_taken]
    min_step=-1
    if steps_to_be_taken < 0:
        dict_mem[steps_to_be_taken]=0
        return 0
    for step in steps:
        if steps_to_be_taken==step:
            dict_mem[steps_to_be_taken]=1
            return 1
    for step in steps:
        ret_val=fetch_minimum_staircase(steps,steps_to_be_taken-step,dict_mem)+1
        if min_step==-1 or min_step>ret_val:
            min_step=ret_val
    dict_mem[steps_to_be_taken]=min_step
    return min_step
if __name__ == "__main__":
    steps=[1,2,3]
    step_size=6
    mem={}
    print(fetch_minimum_staircase(steps,step_size,mem))
    print(mem)