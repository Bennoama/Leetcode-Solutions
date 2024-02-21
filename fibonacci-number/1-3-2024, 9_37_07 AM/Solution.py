// https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:
        nMinus1 = 1
        nMinus2 = 0
        fN = 0
        if (n < 2):
            return n
        for i in range (2, n + 1):
            fN = nMinus1 + nMinus2
            nMinus2 = nMinus1
            nMinus1 = fN
        return fN