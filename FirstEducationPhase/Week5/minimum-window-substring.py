class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        window=defaultdict(int)
        target=defaultdict(int)
        for index in range(len(t)) : 
            target[t[index]]+=1
        for char in range(len(t)) :
            if s[char] in target:
                window[s[char]]+=1
        if window==target:
            return s[:len(t)]
        mnm=float('inf')
        index=["",""]
        left=0
        for right in range(len(t),len(s)):
            if s[right] in target:
                window[s[right]]+=1
            while self.is_valid(window,target):
                if right-left+1 < mnm:
                    index=left,right
                    mnm=right-left+1
                if s[left] in target:
                    window[s[left]]-=1
                    if window[s[left]]==0:
                        window.pop(s[left])
                left+=1
        return s[index[0]:index[1]+1] if mnm < float("inf") else ""
    def is_valid(self,window,target):
        if len(window)!=len(target):
            return False
        for char in target:
            if window[char] < target[char]:
                return False
        return True

                



