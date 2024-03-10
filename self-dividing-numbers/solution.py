class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        numbers = []
        for i in range(left, right + 1):
            curr = i
            shouldInsert = True
            while (curr > 0):
                dig = curr % 10
                if (dig == 0):
                    shouldInsert = False
                    break
                if i % dig != 0:
                    shouldInsert = False
                    break
                curr //= 10
            if shouldInsert:
                numbers.append(i)
        
        return numbers
