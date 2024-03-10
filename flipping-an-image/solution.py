class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        length = len(image)
        for i in range(0, length):
            self.reverseRow(image, i)
        return image

    def reverseRow(self, image: List[List[int]], index:int) -> None:
        right = len(image) - 1
        left = 0
        while (left <= right):
            image[index][left], image[index][right] = image[index][right] ^ 1, image[index][left] ^ 1
            left += 1
            right -= 1
