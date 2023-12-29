class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        s.sort(key= lambda x:x[-1]) 
        answer=""
        for word in s:
            answer+=word[:-1]+" "
        return answer[:-1]