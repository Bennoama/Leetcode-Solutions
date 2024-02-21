// https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings = [''] * numRows
        currRow = 0
        down = True
        for c in s:
            strings[currRow] += c
            if (numRows > 1):
                currRow = currRow + 1 if down else currRow - 1
            if (currRow == numRows - 1 or currRow == 0):
                down = not down

        totalString = ''
        for string in strings:
            totalString += string
        
        return totalString