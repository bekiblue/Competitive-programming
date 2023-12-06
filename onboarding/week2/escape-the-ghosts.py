class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance=abs(target[0])+abs(target[1])
        for ghost in range(len(ghosts)):
           if abs(ghosts[ghost][0]-target[0])+abs(ghosts[ghost][1]-target[1])<=distance:
               return False
        return True
        