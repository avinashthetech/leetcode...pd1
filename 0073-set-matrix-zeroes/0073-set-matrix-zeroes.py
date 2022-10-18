class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
       
# #         row = [1]*len(matrix)
# #         col = [1]*len(matrix[0])
# #         for i in range(len(row)):
# #             for j in range(len(col)):
# #                 if matrix[i][j] == 0:
# #                     row[i] = 0
# #                     col[j] = 0
# #         for i in range(len(row)):
# #             for j in range(len(col)):
# #                 if row[i] == 0 or col[j] == 0:
# #                     matrix[i][j] = 0


#def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = [], []
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    row.append(r)
                    col.append(c)
        
        for r in row:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
        
        for c in col:
            for i in range(len(matrix)):
                matrix[i][c] = 0