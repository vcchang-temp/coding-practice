# Fibonacci

# Input: int n

# Iterative approach
# Time: O(n)  -> iterate through each int of n
# Space: O(1) -> space is not growing according to n

def findNthFibNum(n: int):
    if n <= 1:
        return n
    total, count, prevTotal = 1, 2, 0 # prevTotal = fib(0), total = fib(1)
    while count <= n: # n-1 iterations total b/c already calculated fib(1)
        temp = total
        total += prevTotal
        prevTotal = temp
        count += 1
    return total
        
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