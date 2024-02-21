// https://leetcode.com/problems/find-the-highest-altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currHeight = 0
        maxHeight = 0
        for relHeight in gain:
            currHeight += relHeight
            maxHeight = currHeight if currHeight > maxHeight else maxHeight
        return maxHeight