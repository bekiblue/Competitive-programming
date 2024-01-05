class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lighter=0
        heavier=len(people)-1
        boats=0
        while lighter <= heavier:
            if people[lighter]+people[heavier] <= limit:
                lighter+=1
            heavier-=1
            boats+=1
        return boats