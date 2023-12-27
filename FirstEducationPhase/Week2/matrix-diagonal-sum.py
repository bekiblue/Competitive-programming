class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total=0
        for row in range(len(mat)):
            total+=mat[row][row]+mat[row][len(mat[0])-1-row]
        if len(mat)%2:
            return total-mat[(len(mat)-1)//2][(len(mat)-1)//2]
        return total
            