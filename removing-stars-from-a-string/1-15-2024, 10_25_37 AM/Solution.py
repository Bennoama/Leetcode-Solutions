// https://leetcode.com/problems/removing-stars-from-a-string

class Solution:
    def removeStars(self, s: str) -> str:
        index = s.find('*')
        while (-1 != index):
            s = s[:index - 1] + s[index + 1:]
            index = s.find('*')
        return s