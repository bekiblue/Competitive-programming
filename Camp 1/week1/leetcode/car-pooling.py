class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_km=1000
        prefix=[0]*(max_km+1)
        for trip in trips:
            prefix[trip[1]]+=trip[0]
            prefix[trip[2]]-=trip[0]
        running_sum=0
        for num in prefix:
            running_sum+=num
            if running_sum > capacity:
                return False
        return True
        

        


        
        # trips.sort(key=lambda trip:trip[0])
        # drop=defaultdict(int)
        # current=0 
        # for trip in trips:
        #     current-=drop[trip[1]]
        #     current+=trip[0]
        #     if current > capacity :
        #         return False
        #     drop[trip[1]]+=trip[0]
        # return True