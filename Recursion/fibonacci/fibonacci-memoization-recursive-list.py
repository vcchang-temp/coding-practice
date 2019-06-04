# Fibonacci

# Input: int n

# Memoization-recursive-List approach
# (Memoization = technique often used in dynamic 
# programming to store results and then taking 
# advantage of the stored results to avoid making 
# the same function calls/recalculating results for 
# the same inputs; only need to calculate fib num
# for a given n once)

# Time: O(n)  -> iterate through each int of n
# Space: O(n) -> create new array of len n+1 to
#                store previously calculated fib
#                values

from typing import List

def findNthFibNum(n: int, fibNums: List[int] = [0, 1]):
    if len(fibNums) > n:
        return fibNums[n]
    fibNums.append(findNthFibNum(n-2, fibNums) + findNthFibNum(n-1, fibNums))
    return fibNums[n]

if __name__ == "__main__":
    nZero = 0
    expectedZero = 0
    actualZero = findNthFibNum(nZero)
    assert actualZero == expectedZero
    print(f"The {nZero}th Fibonacci number is {actualZero}.")

    nOne = 1
    expectedOne = 1
    actualOne = findNthFibNum(nOne)
    assert actualOne == expectedOne
    print(f"The {nOne}st Fibonacci number is {actualOne}.")

    n = 6
    expected = 8
    actual = findNthFibNum(n)
    assert actual == expected
    print(f"The {n}th Fibonacci number is {actual}.")

    nLarge = 17
    expectedLarge = 1597
    actualLarge = findNthFibNum(nLarge)
    assert actualLarge == expectedLarge
    print(f"The {nLarge}th Fibonacci number is {actualLarge}.")