def return_sieve(n):
    prime = [True for i in range(n+1)] 
    p = 2
    temp_list=[]
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1

    prime=[i for i in range(len(prime)) if prime[i]]
            
    return prime

def main():
    sieve=return_sieve(4*(10**6))
    testcase=int(input())
    while testcase > 0:
        inp=int(input())
        array=[int(element) for element in input().split(" ")]
        dict_main={}
        sieve_counter=2
        for index in range(inp):
            elem=array[i]
            if elem in dict_main:
                array[index]=dict_main[elem]
            else:
                dict_main[array[index]]=sieve[sieve_counter]
                array[index]=sieve[sieve_counter]
                sieve_counter+=1
        print(*array)

        
if __name__ == "__main__":
    main()