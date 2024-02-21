// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(0, max(nums) + 1):
            if self.arraySpecial(nums, i):
                return i
        return -1

    def arraySpecial(self, nums:List[int], x:int) -> bool:
        count = 0
        for num in nums:
            if (num >= x):
                count += 1
        return count == x