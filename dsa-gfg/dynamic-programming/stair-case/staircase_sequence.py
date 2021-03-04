#!/usr/bin/env python3
def countWays(numberOfStairs, stepCount):
    temp = 0
    result = [1]
    for index in range(1, numberOfStairs + 1):
        tempVar = index - stepCount - 1
        tempVar2 = index - 1
        if tempVar >= 0:
            temp -= result[tempVar]
        temp += result[tempVar2]
        result.append(temp)
    return result[numberOfStairs]


def main():
    numberOfStairsInput = 3
    stepCountInput = 2  # steps:1,2
    print(f"Output: {countWays(numberOfStairsInput, stepCountInput)}")


if __name__ == "__main__":
    main()
