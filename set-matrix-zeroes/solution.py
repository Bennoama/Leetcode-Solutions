class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        points = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    points.append([i, j])
        for point in points:
            i, j = point[0], point[1]
            self.turnRowToZero(matrix, i)
            self.turnColumnToZero(matrix, j)

    def turnRowToZero(self, matrix: List[List[int]], row:int):
        for j in range(len(matrix[0])):
            matrix[row][j] = 0

    def turnColumnToZero(self, matrix: List[List[int]], column:int):
        for i in range(len(matrix)):
            matrix[i][column] = 0
