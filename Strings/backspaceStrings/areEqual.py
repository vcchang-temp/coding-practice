# Backspace strings
# Given two strings S and T, return if they are equal 
# when both are typed into empty text editors. # means 
# a backspace character.

# Time: O(n+m)        -> S = len of n chars, T = len of m chars
# Space: O(max(n, m)) -> storing S and T chars in stacks/arrays/strings

def areEqual(s: str, t: str):
    return applyBackspaces(s) == applyBackspaces(t)

def applyBackspaces(s: str):
    stack = []
    i = 0
    while i < len(s):
        if s[i] != "#":
            stack.append(s[i])
            i += 1
        else:
            if i == 0:
                i += 1
            else:
                while stack and i < len(s) and s[i] == "#":
                    stack.pop()
                    i += 1
    return "".join(stack)

if __name__ == "__main__":
    s = "winnn#ing"
    t = "winning"
    expected = True
    actual = areEqual(s, t)
    assert actual == expected
    print(f"Removed backspaces from {s}: {t}")

    s = "winnn#ing#"
    t = "winnin"
    expected = True
    actual = areEqual(s, t)
    assert actual == expected
    print(f"Removed backspaces from {s}: {t}")

    s = "#winn#ning"
    t = "winning"
    expected = True
    actual = areEqual(s, t)
    assert actual == expected
    print(f"Removed backspaces from {s}: {t}")

    s = "#winn#ning"
    t = "wining"
    expected = False
    actual = areEqual(s, t)
    assert actual == expected
    print(f"Removed backspaces from {s}, but not same as {t} after removal")