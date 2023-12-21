class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for index in range(len(strs[0])):
            for row in range(len(strs)-1):
                if strs[row+1][index] < strs[row][index]:
                    count+=1
                    break
        return count
            
