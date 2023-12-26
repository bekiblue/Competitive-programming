class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        col=defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==".":
                    continue
                if board[r][c] in row[r]:
                    return False
                row[r].add(board[r][c])
                if board[r][c] in col[c]:
                    return False 
                col[c].add(board[r][c])
        for row in range(0,len(board),3):
            for col in range(0,len(board[0]),3):
                cell=set()
                for r in range(row,row+3):
                    for c in range(col,col+3):
                        if board[r][c]==".":
                            continue
                        elif board[r][c] in cell:
                            return False
                        cell.add(board[r][c])
        return True

