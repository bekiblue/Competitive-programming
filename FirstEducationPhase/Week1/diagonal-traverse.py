class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        flag=True
        answer=[]
        for k in range(len(mat)+len(mat[0])-1):
            flag=not flag
            if flag:
                for i in range(len(mat)):
                    if k-i>=0 and k-i < len(mat[0]):
                        answer.append(mat[i][k-i])
            else:
                for i in range(len(mat)-1,-1,-1):
                    if k-i>=0 and k-i < len(mat[0]):
                        answer.append(mat[i][k-i])
        return answer

        