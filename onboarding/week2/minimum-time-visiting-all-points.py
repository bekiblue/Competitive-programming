class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time=0
        for point in range(1,len(points)):
            time+=max(abs(points[point][0]-points[point-1][0]),abs(points[point][1]-points[point-1][1]))
        return time 