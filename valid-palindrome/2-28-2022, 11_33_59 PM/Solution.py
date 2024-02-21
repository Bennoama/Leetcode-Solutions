// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        relavent_data = (''.join(filter(str.isalnum, s))).lower()
        reverse = relavent_data[::-1]
        return relavent_data == reverse