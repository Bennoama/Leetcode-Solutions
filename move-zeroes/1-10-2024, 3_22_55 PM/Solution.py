// https://leetcode.com/problems/move-zeroes

import numpy as np

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        
        for num in nums:
            if (num != 0):
                nums[index] = num
                index += 1
        while (index < len(nums)):
            nums[index] = 0
            index += 1