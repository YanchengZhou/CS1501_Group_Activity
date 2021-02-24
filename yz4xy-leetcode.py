"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once
 and returns the new length.

"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = []
        for i in nums:
            if not i in a:
                a.append(i)
        print(len(a), ',', a)

