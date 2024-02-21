// https://leetcode.com/problems/equal-row-and-column-pairs

import numpy as np

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        columns = []
        for row in grid:
            rows.append(row)

        A = np.array(grid)
        for i in range(0, len(grid)):
            columns.append(A[:,i])
            
        count = 0
        for i in range(0,len(grid)):
            for j in range(0, len(grid)):
                if (self.arraysEqual(rows[i], columns[j])):
                    count += 1
        return count

    def arraysEqual(self, arr1, arr2) -> bool:
        if (len(arr1) != len(arr2)):
            return False
        for i in range(len(arr1)):
            if (arr1[i] != arr2[i]):
                return False
        return True
