class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if self.blackbox(mid, piles, h):
                right = mid
            else:
                left = mid + 1
        return left

    def blackbox(self, maxpiles, piles, h):
        hours = 0
        for i in piles:
            time = i // maxpiles
            hours += time
            if i % maxpiles != 0:
                hours += 1
        return hours <= h
