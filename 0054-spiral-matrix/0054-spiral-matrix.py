class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows,cols=len(matrix),len(matrix[0])
        L=[]
        top,bottom=0,rows-1
        left,right=0,cols-1

        while top<=bottom and left<=right:

            for i in range(left,right+1):
                L.append(matrix[top][i])
            top+=1

            for i in range(top,bottom+1):
                L.append(matrix[i][right])
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    L.append(matrix[bottom][i])
                bottom-=1

            if left<=right:
                for i in range(bottom,top-1,-1):
                    L.append(matrix[i][left])
                left+=1

        return L