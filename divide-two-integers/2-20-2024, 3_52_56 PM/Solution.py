// https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        negMultiplier = 1

        if dividend < 0 and divisor > 0:
            negMultiplier = -1
            dividend = -dividend
        elif dividend > 0 and divisor < 0:
            negMultiplier = -1
            divisor = -divisor
        elif dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor

        numTimes = len(range(0, dividend-divisor + 1, divisor))
        if (negMultiplier == 1 and numTimes > 2 ** 31 - 1):
            return 2 ** 31 - 1
        if (negMultiplier == -1 and -numTimes < -2 ** 31):
            return -2 ** 31
        
        return numTimes if negMultiplier == 1 else -numTimes

    