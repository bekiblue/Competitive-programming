class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left,right+1):
            for interval in ranges:
                if  interval[0] <= num and interval[1] >= num:
                    break
            else:
                return False
        return True
            
            
