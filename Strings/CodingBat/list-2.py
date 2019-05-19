# Practicing Python to learn basic syntax
# https://codingbat.com/python

# List-2
# Medium python list problems -- 1 loop.. 
# Use a[0], a[1], ... to access elements 
# in a list, len(a) is the length.

def count_evens(nums):
  count = 0
  for num in nums:
    if num % 2 == 0:
      count += 1
  return count

def big_diff(nums):
  minNum = nums[0]
  maxNum = nums[0]
  for num in nums:
    minNum = min(minNum, num)
    maxNum = max(maxNum, num)
  return maxNum - minNum

def centered_average(nums):
  minNum = nums[0]
  maxNum = nums[0]

  for num in nums:
    minNum = min(minNum, num)
    maxNum = max(maxNum, num)
  nums.remove(minNum)
  nums.remove(maxNum)
  
  sum = 0
  for num in nums:
    sum += num

  return sum/len(nums)

def sum13(nums):
  sum = 0
  for i in range(len(nums)):
    if (nums[i] == 13) or (i > 0 and nums[i-1] == 13):
      continue
    else:
      sum += nums[i]
  return sum

def sum67(nums):
  sum = 0
  hasSeenASix = False
  for num in nums:
    if hasSeenASix and num == 7:
      hasSeenASix = False
      continue
    if num == 6:
      hasSeenASix = True
    if hasSeenASix:
      continue
    else:
      sum += num
  return sum

def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False