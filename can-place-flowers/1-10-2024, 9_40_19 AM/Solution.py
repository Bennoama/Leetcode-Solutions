// https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        if (len(flowerbed) == 1 and flowerbed[0] == 0 and n <= 1):
            return True
        while (i < len(flowerbed) and n > 0):
            if (0 == flowerbed[i]):
                if (i == 0): #first index
                    if (0 == flowerbed[i + 1]):
                        flowerbed[i] = 1
                        n -= 1
                elif (i == len(flowerbed) - 1): #last index
                    if (0 == flowerbed[i - 1]):
                        n -= 1
                elif (0 == flowerbed[i - 1] and  0 == flowerbed[i + 1]): #anywhere in between
                    n -= 1
                    flowerbed[i] = 1
            i += 1
        return n == 0
