class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = "a"
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = "a"
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "a":
                    matrix[i][j] = 0
        return matrix
