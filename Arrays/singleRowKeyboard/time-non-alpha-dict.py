# Single row keyboard
# Assume keyboard = any order of chars in alphabet

# Dictionary (hashmap) approach
# Time: O(n)  -> iterate through every char in string with n chars
# Space: O(n) -> create dictionary with number of chars (n) key-value mappings

def time(keyboard: str, word: str):
    char_idx_mappings = {}
    for i, char in enumerate(keyboard):
        char_idx_mappings[char] = i
    
    total = char_idx_mappings[word[0]]
    for i in range(1, len(word)):
        total += abs(char_idx_mappings[word[i]] - char_idx_mappings[word[i-1]])
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