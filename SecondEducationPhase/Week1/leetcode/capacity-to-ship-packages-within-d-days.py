class Solution:
    def possibleToShip(self,capacity,weights,days):

        d = 1
        cur_ship = 0 

        for weight in weights:
            if weight > capacity :
                return False
            cur_ship += weight 
            if cur_ship > capacity :
                d += 1
                cur_ship = weight 

        return d <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:


        left = max(weights)
        right = sum(weights)

        while left <= right :

            mid = (left + right ) // 2

            if self.possibleToShip(mid,weights,days):
                right = mid - 1
            else:
                left = mid + 1

        return left




