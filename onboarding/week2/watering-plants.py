class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step=1
        cur_capacity=capacity
        for plant in range(len(plants)):
            cur_capacity-=plants[plant]
            if plant+1 < len(plants) and cur_capacity < plants[plant+1]:
                step+=2*(plant+1)
                cur_capacity=capacity
            if plant != len(plants)-1:
                step+=1
        return step 