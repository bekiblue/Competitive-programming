class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq=[0]*max(costs)
        for cost in costs:
            freq[cost-1]+=1
        sorted_costs=[]
        total=0
        for index in range(len(freq)):
            if freq[index]:
                total+=(index+1)*freq[index]
                if total > coins:
                    return len(sorted_costs)+(coins-(total-(index+1)*freq[index]))//(index+1)
                sorted_costs.extend([index+1]*freq[index])
        return len(costs) 
        
        