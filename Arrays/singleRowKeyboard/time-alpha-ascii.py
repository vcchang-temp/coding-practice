# Single row keyboard
# Assume keyboard = English alphabet

# ASCII approach
# Time: O(n)  -> iterate through every char in string with n chars
# Space: O(1) -> space used remains constant with regards to input

def time(keyboard: str, word: str):
    total = 0
    prevVal = ord("a")
    for letter in word:
        total += abs(ord(letter) - prevVal)
        prevVal = ord(letter)
    return total

if __name__ == "__main__":
    keyboard = "abcdefghijklmnopqrstuvwxyz"

    word = "cba"
    expected = 4
    actual = time(keyboard, word)
    assert actual == expected
    print(f"Uyayyyyyy it takes {actual} 'letter time(s)' to type '{word}'!")

    word = "leetcode"
    expected = 74
    actual = time(keyboard, word)
    assert actual == expected
    print(f"Uyayyyyyy it takes {actual} 'letter time(s)' to type '{word}'!")

    word = "aaaaaaaaaaaa"
    expected = 0
    actual = time(keyboard, word)
    assert actual == expected
    print(f"Uyayyyyyy it takes {actual} 'letter time(s)' to type! '{word}'")