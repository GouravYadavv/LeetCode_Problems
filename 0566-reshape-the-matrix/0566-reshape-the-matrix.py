class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ans = []
        if len(mat) * len(mat[0]) != r * c:
            return mat
        else:
            temp = []
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    temp.append(mat[i][j])
            for i in range(r):
                ans.append(temp[i * c : (i + 1) * c])
            return ans