class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p:p[1])
        arrows=1
        end=points[0][1]
        for point in points:
            if point[0] > end :
                arrows+=1
                end=point[1]   
        return arrows