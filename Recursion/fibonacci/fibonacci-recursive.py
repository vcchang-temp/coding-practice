# Fibonacci

# Input: int n

# Recursive approach
# Time: O(2^n) -> exponential runtime; fib runtime =
#                 number of calls made to fib. Num of
#                 calls made can be modelled in a (binary) 
#                 recursion tree. Each node represents a 
#                 call made. Fib recursion = complete (not 
#                 full) tree. Num of nodes (N) in a complete 
#                 tree = 2^h (full tree) <= N <= (2^(h+1)-1) 
#                 (complete tree) where h = height of tree.
#                 Since num of calls made is represented by 
#                 num of nodes, we can see that Big-O runtime 
#                 of fib is in the range of exponential for a 
#                 given n.
# Space: O(n)  -> memory consumed in recursion is memory
#                 consumed in function call stack. Max mem
#                 consumed is mem consumed when at bottom-
#                 most node of recursion tree. Therefore,
#                 space complexity of recursion is always 
#                 proportional to the max depth of the 
#                 recursion tree. Max tree depth for any
#                 generic (int) n of fib = n-1 and max space
#                 taken on call stack = n -> O(n)
#                     Lvl 0     fib(4)
#                             /        \
#                   Lvl 1   fib(3)     fib(2)
#                          /     \      /    \
#                Lvl 2  fib(2) fib(1) fib(1) fib(0)
#                       /    \
#             Lvl 3  fib(1)  fib(0)

def findNthFibNum(n: int):
    if n <= 1:
        return n
    return findNthFibNum(n-1) + findNthFibNum(n-2)

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