// https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        print(counts)
        numsIndex = 0
        for i in range(0, 3):
            while (counts[i] != 0):
                nums[numsIndex] = i
                counts[i] -= 1
                numsIndex += 1
