class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        prev=self.getRow(rowIndex-1)
        cur=[1]*(len(prev)+1)
        for index in range(1,len(prev)):
            cur[index]=prev[index-1]+prev[index]
        return cur

    
            
