// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        addTrailing = True
        while (i >= 0):
            if (digits[i] == 9):
                digits[i] = 0
            else:
                digits[i] += 1
                addTrailing = False
                break
            i -= 1
        if (addTrailing):
            digits.insert(0, 1)
        return digits