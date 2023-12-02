class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n+1)
        for i,j,k in bookings:
            prefix[i-1] += k
            prefix[j] -= k
        for i in range(1, n):
            prefix[i] += prefix[i-1]
        return prefix[:-1]
        
