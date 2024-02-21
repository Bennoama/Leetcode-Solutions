// https://leetcode.com/problems/find-numbers-with-even-number-of-digits

class Solution:
    def isNumDigits(self, num:int) -> bool:
        numDigits = 0
        while (num >= 1):
            numDigits += 1
            num //= 10
        return (numDigits % 2 == 0)

    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if (self.isNumDigits(num)):
                count += 1
        return count