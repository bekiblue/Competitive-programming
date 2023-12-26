class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        col=defaultdict(set)
        cell=defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if board[r][c] in row[r]:
                    return False
                row[r].add(board[r][c])
                if board[r][c] in col[c]:
                    return False 
                col[c].add(board[r][c])
                if board[r][c] in cell[(r//3,c//3)]:
                    return False
                cell[(r//3,c//3)].add(board[r][c])
        
        return True

