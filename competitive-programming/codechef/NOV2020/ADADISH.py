def main():
    testcase=int(input())
    while testcase > 0:
        inp=int(input())
        array=[int(element) for element in input().split(" ")]
        array.sort(reverse=True)
        first=0
        second=0
        for i in range(inp):
            if first<second:
                first+=array[i]
            else:
                second+=array[i]
        print(max(first,second))
        testcase-=1
if __name__ == "__main__":
    main()