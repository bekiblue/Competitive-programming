class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        mon_incr=[] #strictly increasing
        answer=[] 
        for index,price in enumerate(prices):
            answer.append(price)
            while mon_incr and price <= prices[mon_incr[-1]]:
                popped_index=mon_incr.pop()
                answer[popped_index]-=price
            mon_incr.append(index)
        return answer 
