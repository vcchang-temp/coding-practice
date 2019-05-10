# FizzBuzz: write a program that returns a list of string representations
# of numbers 1 to n. For multiples of 3, add "Fizz" to the list; for 
# multiples of 5, add "Buzz" to the list; for multiples of both 3 and 5,
# add "FizzBuzz" to the list.

def fizzbuzz(n: int):
    list = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("FizzBuzz")
        elif i % 3 == 0:
            list.append("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")
        else:
            list.append(str(i))
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
    assert expected == fizzbuzz(num)
    print("FizzBuzz success, huzzah!")