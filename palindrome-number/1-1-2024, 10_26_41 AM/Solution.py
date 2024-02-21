// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        number = str(x)
        length = len(number)
        for i in range(0, length):
            if (number[i] != number[length - i - 1]):
                return False
        return True        
        