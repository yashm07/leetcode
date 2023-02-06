class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_cell = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        new_cell = 0
                    else:
                        matrix[i][0] = 0

        print(matrix, new_cell)
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
                
                if new_cell == 0 and i == 0:
                    matrix[i][j] = 0
                
                elif matrix[i][0] == 0 and i > 0:
                    matrix[i][j] = 0
        