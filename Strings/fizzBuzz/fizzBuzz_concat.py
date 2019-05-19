# FizzBuzz

# Write a program that returns a list of string representations
# of numbers 1 to n. For multiples of 3, add "Fizz" to the list; for 
# multiples of 5, add "Buzz" to the list; for multiples of both 3 and 5,
# add "FizzBuzz" to the list.

# Input: non-negative integer n

# Concat approach
# Slightly more sophisticated logic that allows for more strings to be
# added without having a case for each combination
# Time: O(n) -> must iterate through all nums of n
# Space: O(1) -> storage bounded by constant

def fizzBuzz(n: int):
    list = []

    for i in range(1, n+1):
        fBStr = ""
        if i % 3 == 0:
            fBStr += "Fizz"
        if i % 5 == 0:
            fBStr += "Buzz"
        if not fBStr:
            fBStr += str(i)
        list.append(fBStr)

    return list

if __name__ == "__main__":
    num = 15
    expected = [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]
    assert expected == fizzBuzz(num)
    print("FizzBuzz success, huzzah!")