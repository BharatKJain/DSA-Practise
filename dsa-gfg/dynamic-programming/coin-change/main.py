import sys
from time import perf_counter
#recursive approach
def min_coins(amount,coins):
    if amount == 0:
        return 0
    coins_min=-1
    for coin in coins:
        if amount-coin >=0:
            answer=min_coins(amount-coin,coins) #change condition, with recursive call
            if coins_min==-1 or coins_min>answer:
                coins_min=(answer+1) #Updation condition, when min_coins(0,coins) then we add 1
    return coins_min
mem_dict={}
#optimized approach
def optimized_min_coins(amount,coins,mem_dictionary):
    coins_min=-1
    if amount==0:
        return 0
    if amount in mem_dictionary:
        return mem_dictionary[amount]
    for coin in coins:
        if amount-coin >=0:
            answer=optimized_min_coins(amount-coin,coins,mem_dict) #change condition, with recursive call
            if coins_min==-1 or coins_min>answer:
                coins_min=(answer+1) #Updation condition, when min_coins(0,coins) then we add 1
    mem_dict[amount]=coins_min
    return coins_min
if __name__ == "__main__":
    # input()
    coins=[1,7,10]
    money=65
    start_time=perf_counter()
    print(min_coins(money,coins))
    print(f"For recursive call: {perf_counter()-start_time}")
    start_time=perf_counter()
    print(optimized_min_coins(money,coins,mem_dict))
    print(f"For optimized call: {perf_counter()-start_time}")
