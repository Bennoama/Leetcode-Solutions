class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        small = ""
        large = ""
        if len(num1) < len(num2):
            small, large = num1, num2 
        else:
            small, large = num2, num1
        small = "0" * (len(large) - len(small)) + small

        addOne = 0
        res = ""
        for i in range(len(large) - 1, -1, -1):
            currRes = int(large[i]) + int(small[i]) + addOne
            res += str(currRes % 10)
            addOne = currRes // 10

        if (addOne):
            res += "1"
        return res[::-1]
            
