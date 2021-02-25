"""
Given an array nums and a value val, 
remove all instances of that value in-place and return the new length
"""


class Solution:
    def removeElement(self, nums: int, val: int) -> int:
        for i in nums[:]:
            if i == val:
                nums.remove(i)
        return len(nums)
        
