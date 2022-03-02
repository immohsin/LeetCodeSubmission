class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        
        # set all row zero
        for r in rows:
            matrix[r] = [0] * col
 
        # set all col zero
        for i in range(row):
            for c in cols:
                matrix[i][c] = 0
            