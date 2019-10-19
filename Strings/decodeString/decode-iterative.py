# Decode string

# Iterative approach
# Time: O(n)  -> iterate through each char in s of len n
# Space: O(n) -> store at most n chars on stack

def decode(s: str):
    if not s:
        return ''
    stack = []
    for char in s:
        if char != ']':
            stack.append(char)
        else:
            eS = ''
            while stack:
                eSChar = stack.pop()
                if eSChar != '[':
                    eS = eSChar + eS
                else:
                    num = ''
                    while stack and stack[-1].isdigit():
                        num = stack.pop() + num
                    stack.append(eS * int(num))
                    break
    return ''.join(stack)

if __name__ == "__main__":
    s = "3[a]2[bc]"
    expected = "aaabcbc"
    actual = decode(s)
    assert actual == expected
    print(f"Woot, decoded {s} into {actual}!")

    s = "3[a2[c]]"
    expected = "accaccacc"
    actual = decode(s)
    assert actual == expected
    print(f"Woot, decoded {s} into {actual}!")

    s = "3[a]2[bc]"
    expected = "aaabcbc"
    actual = decode(s)
    assert actual == expected
    print(f"Woot, decoded {s} into {actual}!")
