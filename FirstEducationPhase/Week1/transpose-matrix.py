class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        answer=[]
        for row in range(len(matrix[0])):
            answer.append([])
            for col in range(len(matrix)):
                answer[row].append(matrix[col][row])
        return answer