// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        elif haystack.count(needle)==0:
                return -1
        else:
                return haystack.index(needle)