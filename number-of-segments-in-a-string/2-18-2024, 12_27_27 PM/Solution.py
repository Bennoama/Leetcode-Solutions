// https://leetcode.com/problems/number-of-segments-in-a-string

class Solution:
    def countSegments(self, s: str) -> int:
        parts = s.split(' ')
        count = 0
        for part in parts:
            if part != "":
                count += 1
        return count