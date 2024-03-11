class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        [rookRow, rookCol] = self.findRookPosition(board)
        numCaptures = 0
        numCaptures += self.capturesInDirection(board, [-1, 0], [rookRow, rookCol])
        numCaptures += self.capturesInDirection(board, [1, 0], [rookRow, rookCol])
        numCaptures += self.capturesInDirection(board, [0, 1], [rookRow, rookCol])
        numCaptures += self.capturesInDirection(board, [0, -1], [rookRow, rookCol])
        return numCaptures
    
    def findRookPosition(self, board: List[List[str]]) -> List[int]:
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 'R':
                    return [i, j]
        return [-1, -1]

    def capturesInDirection(self, board: List[List[str]], direction: List[int], startPos: List[int]) -> int:
        row = startPos[0] + direction[0]
        column = startPos[1] + direction[1]
        while (row >= 0 and row < 8 and column < 8 and column >= 0):
            if board[row][column] == 'p':
                return 1
            if board[row][column] == 'B':
                return 0
            row += direction[0]
            column += direction[1]
        return 0
