# Move Zeroes
# (Has to move them in-place)

# Time: 
# Space: 

from typing import List

def moveZeroes(nums: List[int]):
    follower = leader = 0
        
    while leader < len(nums):
        if nums[follower] == 0:
            while leader < len(nums) and nums[leader] == 0:
                leader += 1
            if leader == len(nums):
                return
            nums[follower], nums[leader] = nums[leader], nums[follower]
            follower += 1
        else:
            follower += 1
            leader += 1

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    expected = [1,3,12,0,0]
    moveZeroes(nums)
    assert nums == expected
    print(f"Moved all zeroes to the end: {nums}")

    nums = [3,1,0,0,0]
    expected = [3,1,0,0,0]
    moveZeroes(nums)
    assert nums == expected
    print(f"Moved all zeroes to the end: {nums}")

    nums = [0,0,0,3,12]
    expected = [3,12,0,0,0]
    moveZeroes(nums)
    assert nums == expected
    print(f"Moved all zeroes to the end: {nums}")

    nums = []
    expected = []
    moveZeroes(nums)
    assert nums == expected
    print(f"Moved all zeroes to the end: {nums}")

    nums = [0,0,0]
    expected = [0,0,0]
    moveZeroes(nums)
    assert nums == expected
    print(f"Moved all zeroes to the end: {nums}")