class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        mxm=0
        for point in range(len(points)-1):
            mxm=max(mxm,points[point+1][0]-points[point][0])
        return mxm 