from pyrival.algebra import sieve
from pyrival.combinatorics import partitions
def main():
    print(list(sieve.prime_list(1000)))
    print(partitions(10,2))
if __name__ =="__main__":
    main()