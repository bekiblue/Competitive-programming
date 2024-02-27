class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ticket_left=tickets[k]
        tickets[k]="p"
        tickets=deque(tickets)
        time=0
        while ticket_left:
            val=tickets.popleft()
            if val != "p":
                val-=1
            else:
                ticket_left-=1
            if val != 0:
                tickets.append(val)
            time+=1
        return time

