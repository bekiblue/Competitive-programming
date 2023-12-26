class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(row,len(matrix[0])):
                matrix[row][col],matrix[col][row]=matrix[col][row],matrix[row][col]
            left,right=0,len(matrix[0])-1
            while left<right:
                matrix[row][left],matrix[row][right]=matrix[row][right],matrix[row][left]
                left+=1
                right-=1

        
