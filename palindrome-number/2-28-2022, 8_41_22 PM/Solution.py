// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x==0:
            return True
        else:
            x_string = str(x)
            length = len(x_string)
            for i in range(length):
                if x_string[i] != x_string[length-1-i]:
                    return False
            return True
                