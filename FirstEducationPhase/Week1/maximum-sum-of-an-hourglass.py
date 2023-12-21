class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        mxm=0
        for row in range(len(grid)-2):
            start=0
            for col in range(len(grid[0])-2):
                top=sum(grid[row][start:col+3])
                middle=grid[row+1][start+1]
                bottom=sum(grid[row+2][start:col+3])
                mxm=max(top+middle+bottom,mxm)
                start+=1
        return mxm 