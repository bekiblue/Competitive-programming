class Solution:
    def sortSentence(self, s: str) -> str:
        temp=s.split()
        answer=temp.copy()
        for word in temp :
           answer[int(word[-1])-1]=word[:-1]
        sorted=" ".join(answer)
        return sorted
