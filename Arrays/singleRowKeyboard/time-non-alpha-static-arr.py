# Single row keyboard
# Keyboard = any string keyboard containing each 
# English lowercase letter exactly once in some order.

# ASCII approach (any alpha)
# Time: O(n)  -> iterate through every char in string with n chars
# Space: O(n) -> space used will be equal to number of chars in keyboard (n)

def time(keyboard: str, word: str):
    # Encode data
    # data stores the position of each char in the keyboard
    # eg: keyboard = "pqrstu", r = at 2nd pos (index) in keyboard
    # We standardize each char against ASCII to fit them into a 26-char array
    # Otherwise we'd waste a lot of space, as lowercase English char ASCII
    # go from 97-122, so data would be arr of len 122
    data = [None] * len(keyboard)
    for i, char in enumerate(keyboard):
        data[ord(char) - 97] = i
    
    # Calculate letter distances in word using data
    total = data[ord(word[0]) - 97]
    for i in range(1, len(word)):
        currCharPosInKeyboard = data[ord(word[i]) - 97]
        prevCharPosInKeyboard = data[ord(word[i-1]) - 97]
        total += abs(currCharPosInKeyboard - prevCharPosInKeyboard)
    return total

if __name__ == "__main__":
    keyboard = "pqrstuvwxyzabcdefghijklmno"

    word = "cba"
    expected = 15
    actual = time(keyboard, word)
    assert actual == expected
    print(f"Uyayyyyyy it takes {actual} 'letter time(s)' to type '{word}'!")

    word = "leetcode"
    expected = 73
    actual = time(keyboard, word)
    assert actual == expected
    print(f"Uyayyyyyy it takes {actual} 'letter time(s)' to type '{word}'!")

    word = "aaaaaaaaaaaa"
    expected = 11
    actual = time(keyboard, word)
    assert actual == expected
    print(f"Uyayyyyyy it takes {actual} 'letter time(s)' to type! '{word}'")

    keyboard = "oqrmauewvyztbcdxfkgijhlsnp"
    word = "cba"
    expected = 22
    actual = time(keyboard, word)
    assert actual == expected
    print(f"Uyayyyyyy it takes {actual} 'letter time(s)' to type '{word}'!")

    word = "leetcode"
    expected = 80
    actual = time(keyboard, word)
    assert actual == expected
    print(f"Uyayyyyyy it takes {actual} 'letter time(s)' to type '{word}'!")

    word = "aaaaaaaaaaaa"
    expected = 4
    actual = time(keyboard, word)
    assert actual == expected
    print(f"Uyayyyyyy it takes {actual} 'letter time(s)' to type! '{word}'")