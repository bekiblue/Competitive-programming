class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[]
        for point in points:
            distance.append(point[0]*point[0]+point[1]*point[1])
        
        for i in range(len(distance)):
            min=i
            for j in range(i+1,len(distance)):
                if distance[j]<distance[min]:
                    min=j
            distance[i],distance[min]=distance[min],distance[i]  
            points[i],points[min]=points[min],points[i]  
        return points[0:k]
