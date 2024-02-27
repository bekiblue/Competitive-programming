class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        desire=tickets[k]
        for index,ticket in enumerate(tickets):
            if index <= k :
                time+=min(ticket,desire)
            else:
                time+=min(ticket,desire-1)
        return time



