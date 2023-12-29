class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for slow in range(len(names)-1):
            mxm=slow
            for fast in range(slow+1,len(names)):
                if heights[fast] > heights[mxm]:
                    mxm=fast
            if mxm!=slow:
                names[slow],names[mxm]=names[mxm],names[slow]
                heights[slow],heights[mxm]=heights[mxm],heights[slow]
        return names
        
            