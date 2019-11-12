# Excel Sheet Column Number

# Time: O(n)  -> visit each char of string of len n twice
#                (once through .reversed(), once through for loop)
# Space: O(n) -> create new string through .reversed()

def calculateColNum(s: str):
    res = 0
    for i, c in enumerate(reversed(s)):
        val = ord(c) - 64
        res += (26**i) * val # working in base 26; val = how many rounds of letters have to wait before it's c
    return res

if __name__ == "__main__":
    s = "A"
    expected = 1
    actual = calculateColNum(s)
    assert actual == expected
    print(f"Column number of {s} is {actual}.")

    s = "AB"
    expected = 28
    actual = calculateColNum(s)
    assert actual == expected
    print(f"Column number of {s} is {actual}.")

    s = "AAA"
    expected = 703
    actual = calculateColNum(s)
    assert actual == expected
    print(f"Column number of {s} is {actual}.")