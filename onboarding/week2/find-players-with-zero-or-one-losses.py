class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero,one,many=set(),set(),set()
        for winner,loser in  matches:
            if winner not in one and  winner not in many:
                zero.add(winner)
            if loser in zero :
                zero.remove(loser)
                one.add(loser)
            elif loser in one:
                one.remove(loser)
                many.add(loser)
            elif loser not in zero and loser not in many:
                one.add(loser)
            
        return [sorted(list(zero)),sorted(list(one))]
            
                

