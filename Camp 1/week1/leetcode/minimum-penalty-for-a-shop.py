class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix=[]
        running_sum=0
        for customer in customers:
            prefix.append(running_sum)
            if customer=="N":
                running_sum+=1
        mnm=running_sum
        answer=len(customers)
        running_sum=0
        for index in range(len(customers)-1,-1,-1):
            if customers[index]=="Y":
                running_sum+=1
            if running_sum+prefix[index] <= mnm:
                answer=index
                mnm=running_sum+prefix[index]
        return answer
        
            

        
        