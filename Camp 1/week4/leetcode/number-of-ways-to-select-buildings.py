class Solution:
    def numberOfWays(self, s: str) -> int:
        possible_buildings_before=[]
        office=0
        restaurant=0
        for building in s:
            if building == "0":
                office+=1
                possible_buildings_before.append(restaurant)
            else:
                restaurant+=1
                possible_buildings_before.append(office)
        answer=0
        office=0
        restaurant=0
        for building in range(len(s)-1,-1,-1):
            if s[building]=="0":
                office+=1
                answer+=(restaurant*(possible_buildings_before[building]))
            else:
                restaurant+=1
                answer+=(office*(possible_buildings_before[building]))
        return answer


        
        
       
             
            
            