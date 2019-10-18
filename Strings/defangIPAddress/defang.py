# Defang IP address
# Assume given valid IP address

# Time: O(n)  -> split() takes up most time; n = len(address) and m = len of separator
#                = O(mn) ~= O(n)
# Space: O(n) -> create new list and string with two more chars per 3-char decimal group
#                = 4 groups * 3 chars + 4 groups * 2 chars ([]) + 4 groups * 1 char (.)
#                = 24 chars, vs. 16 chars before
#                = n + 1/3n = 4/3n ~= O(n)

def defangIPaddr(address: str):
    return "[.]".join(address.split("."))