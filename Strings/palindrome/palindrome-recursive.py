# Palindrome check

# Palindrome: string spelt the same forwards and backwards

# Input: non-empty string s

# Assumptions: no spaces in s

# Recursive approach
# Time: O(n)  -> go through n/2 chars -> O(n/2) ~= O(n)
# Space: O(n) -> memory usage from recursion; call stack building
#                up with each recursive call being stored on stack

def isPalindrome(s: str, startIndex: int = 0):
    endIndex = len(s) - 1 - startIndex
    return True if startIndex >= endIndex else s[startIndex] == s[endIndex] and isPalindrome(s, startIndex + 1)

if __name__ == "__main__":
    evenPalindrome = "anna"
    actualEven = isPalindrome(evenPalindrome)
    assert actualEven == True
    print("Yeayy, a palindrome with an even count of characters!")

    oddPalindrome = "racecar"
    actualOdd = isPalindrome(oddPalindrome)
    assert actualEven == True
    print("Wooo, a palindrome with an odd count of characters!")

    notAPalindrome = "anstna"
    actualNotP = isPalindrome(notAPalindrome)
    assert actualNotP == False
    print("Boo, not a palindrome :'(")