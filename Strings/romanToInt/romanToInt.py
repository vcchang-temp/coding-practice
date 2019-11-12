# Roman to Integer

# Time: O(n)  -> visit each char in roman numeral of len n twice 
# Space: O(n) -> create stack of len n chars

def romanToInt(s: str):
    stack, i = [], 0
    roman_int = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
        
    while i < len(s):
        stack.append(s[i])
        i += 1
        
    res = 0
    while stack:
        roman = stack.pop()
        res += roman_int[roman]
        if not stack:
            break
        nextRoman = stack[-1]
        if roman_int[nextRoman] < roman_int[roman]:
            res -= roman_int[nextRoman]
            stack.pop()
    return res

if __name__ == "__main__":
    r = "III"
    expected = 3
    actual = romanToInt(r)
    assert actual == expected
    print(f"Converted roman {r} to integer: {actual}")

    r = "LVIII"
    expected = 58
    actual = romanToInt(r)
    assert actual == expected
    print(f"Converted roman {r} to integer: {actual}")

    r = "MCMXCIV"
    expected = 1994
    actual = romanToInt(r)
    assert actual == expected
    print(f"Converted roman {r} to integer: {actual}")