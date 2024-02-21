// https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        string_n = str(binary)
        return(string_n.count('1'))