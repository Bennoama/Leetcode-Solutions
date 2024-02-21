// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while (i * i < x):
            i += 1
        return i if i * i == x else i - 1