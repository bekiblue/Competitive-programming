class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split()
        mxm=len(max(words,key=len))
        answer=[]
        for index in range(mxm):
            vertical=""
            for word in words:
                if index < len(word):
                    vertical+=word[index]
                else:
                    vertical+=" "
            answer.append(vertical.rstrip())
        return answer
