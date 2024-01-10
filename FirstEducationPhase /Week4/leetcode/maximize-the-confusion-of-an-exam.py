class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        longest=0
        #Handling for the True
        used=0
        left=0
        for right in range(len(answerKey)):
            if answerKey[right]=="F":
                used+=1
            while used > k:
                if answerKey[left]=="F":
                    used-=1
                left+=1
            longest=max(longest,right-left+1)
         #Handling for the False
        used=0
        left=0
        for right in range(len(answerKey)):
            if answerKey[right]=="T":
                used+=1
            while used > k:
                if answerKey[left]=="T":
                    used-=1
                left+=1
            longest=max(longest,right-left+1)
        return longest
        
        

                
                