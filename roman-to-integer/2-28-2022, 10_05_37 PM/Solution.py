// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        sub_total = 0
        dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for index, c in enumerate(s):
            if index == 0 or c == s[index-1]:
                sub_total+=dictionary[c]
            elif dictionary[s[index-1]] < dictionary[c]:
                total += dictionary[c] - sub_total
                sub_total = 0
            else:
                total += sub_total
                sub_total = dictionary[c]
                
        return total + sub_total