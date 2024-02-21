// https://leetcode.com/problems/perfect-number


import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1: return False
        sumDivisors = 1
        i = 2
        while i*i < num:
            if num % i == 0: sumDivisors += i + num // i
            i += 1
        if i * i == num: sumDivisors += i
        return sumDivisors==num
