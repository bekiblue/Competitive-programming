class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target=defaultdict(int)
        window=defaultdict(int)
        answer=[]
        if len(s) < len(p):
            return answer
        for char in range(len(p)):
            target[p[char]]+=1
            window[s[char]]+=1
        if target==window:
            answer.append(0)
        for index in range(len(p),len(s)):
            window[s[index-len(p)]]-=1
            window[s[index]]+=1
            if window[s[index-len(p)]]==0:
                window.pop(s[index-len(p)])
            if target==window:
                answer.append(index-len(p)+1)
        return answer 
            
