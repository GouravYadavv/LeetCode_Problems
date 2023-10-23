class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rows,cols=n,n

        matrix=[[0 for _ in range(cols)] for _ in range(rows)]

        top=0
        bottom=rows-1
        left=0
        right=cols-1

        num=1

        while top<=bottom and left<=right:
            for col in range(left,right+1):
                matrix[top][col]=num
                num+=1
            top+=1

            for row in range(top,bottom+1):
                matrix[row][right]=num
                num+=1
            right-=1

            for col in range(right,left-1,-1):
                matrix[bottom][col]=num
                num+=1
            bottom-=1

            for row in range(bottom,top-1,-1):
                matrix[row][left]=num
                num+=1
            left+=1

        return matrix