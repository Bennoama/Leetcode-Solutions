class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(rows[i - 1][j - 1] + rows[i - 1][j])
            row.append(1)
            rows.append(row)
        return rows
