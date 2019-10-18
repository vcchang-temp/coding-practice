# Split a string in balanced strings

# Time: 
# Space: 

def split(s: str):
    if len(s) == 0:
        return 0
    
    count = 0
    diff = 0
    for char in s:
        if char == 'L':
            diff += 1
        else:
            diff -= 1
        
        if diff == 0: # have a balanced substring
            count += 1
    return count

if __name__ == "__main__":
    s = "RLRRLLRLRL"
    expected = 4
    actual = split(s)
    assert actual == expected
    print(f"Split {s} into {actual} LR/RL strings!")

    s = "RLLLLRRRLR"
    expected = 3
    actual = split(s)
    assert actual == expected
    print(f"Split {s} into {actual} LR/RL strings!")

    s = "LLLLRRRR"
    expected = 1
    actual = split(s)
    assert actual == expected
    print(f"Split {s} into {actual} LR/RL strings!")

    s = "RRLRRLRLLLRL"
    expected = 2
    actual = split(s)
    assert actual == expected
    print(f"Split {s} into {actual} LR/RL strings!")