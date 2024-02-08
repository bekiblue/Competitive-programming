class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats=[0]*(n+1)
        for left,right,seat in bookings:
            seats[left-1]+=seat
            seats[right]-=seat
        net_seat=[]
        running_sum=0
        for index in range(n):
            running_sum+=seats[index]
            net_seat.append(running_sum)
        return net_seat


