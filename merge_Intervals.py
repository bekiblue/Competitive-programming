class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        start = []
        end = []
        for lst in intervals:
            start.append(lst[0])
            end.append(lst[1])
        start.sort()
        end.sort()
        s = e = -1
        for i in range(len(start)):
            if e >= start[i]:
                e = end[i]
                res[-1] = [s, e]
            else:
                s = start[i]
                e = end[i]
                res.append([s, e])
        return res
