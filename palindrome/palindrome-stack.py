# Palindrome check

# Palindrome: string spelt the same forwards and backwards

# Input: non-empty string s

# Assumptions: no spaces in s

# Stack approach
# Time: O(n)  -> check each character in s of len n
# Space: O(n) -> stack needs at most n/2 space -> O(n/2) ~= O(n)

import math

def isPalindrome(s: str):
    stack = []
    halfway = math.floor(len(s)/2)
    for i in range(0, halfway):
        stack.append(s[i])
    
    start = halfway if len(s) % 2 == 0 else halfway + 1

    for i in range(start, len(s)):
        if stack.pop() != s[i]:
            return False
    else:
        return True

if __name__ == "__main__":
    evenPalindrome = "hannah"
    actualEven = isPalindrome(evenPalindrome)
    assert actualEven == True
    print("Yeayy, a palindrome with an even count of characters!")

    oddPalindrome = "radar"
    actualOdd = isPalindrome(oddPalindrome)
    assert actualEven == True
    print("Wooo, a palindrome with an odd count of characters!")

    notAPalindrome = "blah"
    actualNotP = isPalindrome(notAPalindrome)
    assert actualNotP == False
    print("Boo, not a palindrome :'(")