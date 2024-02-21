// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        array = []
        new_number = n
        while(new_number != 1):
            new_number = sum(int(c) ** 2 for c in str(new_number))
            if new_number not in array:
                array.append(new_number)
            else:
                return False
        return True
    