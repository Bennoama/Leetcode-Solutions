// https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(0, n + 1):
            arr.append(self.countNumBitsOn(i))
        return arr

    def countNumBitsOn(self, num: int) -> int:
        count = 0
        while (num):
            num &= num - 1
            count += 1
        return count