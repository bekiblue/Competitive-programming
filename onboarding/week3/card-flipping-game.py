class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        not_good=set()
        for card in range(len(backs)):
            if fronts[card]==backs[card]:
                not_good.add(backs[card])
        answer=2001
        backs.extend(fronts)
        for num in backs:
            if num not in not_good:
                answer=min(answer,num)
        if answer < 2001 :
            return answer
        else :
            return 0


