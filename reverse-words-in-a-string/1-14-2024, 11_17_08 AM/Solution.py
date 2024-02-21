// https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        newStr = ""
        for word in reversed(words):
            newStr += word + " "
        return newStr[:-1]