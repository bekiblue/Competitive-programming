class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for slow in range(0,len(names)-1):
            for fast in range(slow+1,len(names)):
                if heights[slow] < heights[fast]:
                     heights[slow],heights[fast]=heights[fast],heights[slow]
                     names[slow],names[fast]=names[fast],names[slow]
        return names

                
