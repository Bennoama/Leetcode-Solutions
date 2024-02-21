// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_value = 0
        for number in nums:
            xor_value ^= number
        return xor_value