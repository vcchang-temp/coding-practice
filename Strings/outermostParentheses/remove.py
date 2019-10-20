# Remove outermost parentheses

# Input: string s that's either empty or a string 
#        with one or more valid parentheses strings
#        (ie: a string that has at least one 
#        primitive parentheses -> "()")

# Time: O(n)  -> iterate through each char in s of len n
# Space: O(n) -> make new string of appox n chars

def removeOuterParentheses(S: str) -> str:
    completeCount = 0 # keeps track of when have a full primitive string
    result = []
    completeStart = 0
    for i in range(len(S)):
        if S[i] == '(':
            completeCount += 1
        if S[i] == ')':
            completeCount -= 1
        if completeCount == 0:
            result.extend(S[completeStart+1 : i]) # remove outermost ()
            completeStart = i+1
    return "".join(result)

if __name__ == "__main__":
    s = "()"
    expected = ""
    actual = removeOuterParentheses(s)
    assert actual == expected
    print(f"Removed outermost parenthesis from {s}: {actual}")

    s = "((())())"
    expected = "(())()"
    actual = removeOuterParentheses(s)
    assert actual == expected
    print(f"Removed outermost parenthesis from {s}: {actual}")