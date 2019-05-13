# Practicing Python to learn basic syntax
# https://codingbat.com/python

# List-1
# Basic python list problems -- no loops.. Use a[0], a[1], ... to access elements in a list, len(a) is the length.

def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[-1]

def make_pi():
  return [3, 1 ,4]

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
  return nums[0] + nums[1] + nums[2]

def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

def max_end3(nums):
  larger = max(nums[0], nums[2])
  nums[0] = larger
  nums[1] = larger
  nums[2] = larger
  return nums

def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return nums[0]
  else:
    return nums[0] + nums[1]

def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
  return [nums[0], nums[-1]]

def has23(nums):
  contains2 = nums[0] == 2 or nums[1] == 2
  contains3 = nums[0] == 3 or nums[1] == 3
  return contains2 or contains3