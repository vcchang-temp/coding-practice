# Fibonacci

# Input: int n

# Memoization-recursive-dict approach
# (Memoization = technique often used in dynamic 
# programming to store results and then taking 
# advantage of the stored results to avoid making 
# the same function calls/recalculating results for 
# the same inputs; only need to calculate fib num
# for a given n once)

# Time: O(n)  -> iterate through each int of n
# Space: O(n) -> create new dict with n+1 keys to
#                store previously calculated fib
#                values

def findNthFibNum(n: int, fibNums: dict = {0: 0, 1: 1}):
    if n in fibNums:
        return fibNums[n]
    fibNums[n] = findNthFibNum(n-2, fibNums) + findNthFibNum(n-1, fibNums)
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