class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans=0
        for i in range(len(mat)):
            j=len(mat[0])-1
            if len(mat)%2!=0 and i==len(mat)//2:
                ans+=mat[i][i]
            else:
                ans+=mat[i][i]+mat[i][j-i]
        return ans