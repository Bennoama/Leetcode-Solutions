class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        answer = matrix
        for columnIndex in range(0, len(answer[0])):
            minuses = []
            colMax = -1
            for rowIndex in range(0, len(answer)):
                if answer[rowIndex][columnIndex] > colMax:
                    colMax = answer[rowIndex][columnIndex]
                if answer[rowIndex][columnIndex] == -1:
                    minuses.append(rowIndex)
            for minus in minuses:
                answer[minus][columnIndex] = colMax
        return answer
                
            
