# Split into L, R strings
# Return maximum number of L, R substrings 

# Time: O(n)  -> iterate through each char in given s of len n
# Space: O(n) -> build stack of at most len n

def split(s: str):
    result = 0
    stack = []
    i = 0
    while i < len(s):
        if len(stack) == 0 and s[i] == 'L':
            while i < len(s) and s[i] == 'L':
                stack.append(s[i])
                i += 1
            continue
        if len(stack) == 0 and s[i] == 'R':
            while i < len(s) and s[i] == 'R':
                stack.append(s[i])
                i += 1
            continue
            
        if stack[-1] == 'L' and s[i] == 'R':
            result += 1
            while len(stack) != 0:
                stack.pop()
            i += 1
        elif stack[-1] == 'R' and s[i] == 'L':
            result += 1
            while len(stack) != 0:
                stack.pop()
            i += 1
    return result

if __name__ == "__main__":
    s = "RLRRLLRLRL"
    expected = 4
    actual = split(s)
    assert actual == expected
    print(f"Split {s} into {actual} L, R/R, L substrings!")

    s = "RLLLLRRRLR"
    expected = 3
    actual = split(s)
    assert actual == expected
    print(f"Split {s} into {actual} L, R/R, L substrings!")

    s = "LLLLRRRR"
    expected = 1
    actual = split(s)
    assert actual == expected
    print(f"Split {s} into {actual} L, R/R, L substrings!")

    s = "RRLRRLRLLLRL"
    expected = 4
    actual = split(s)
    assert actual == expected
    print(f"Split {s} into {actual} L, R/R, L substrings!")