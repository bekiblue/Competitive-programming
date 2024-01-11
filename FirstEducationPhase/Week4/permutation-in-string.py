class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_freq=defaultdict(int)
        s2_freq=defaultdict(int)
        for index in range(len(s1)):
            s1_freq[s1[index]]+=1
            s2_freq[s2[index]]+=1
        if s1_freq==s2_freq:
            return True
        for right in range(len(s1),len(s2)):
            s2_freq[s2[right]]+=1
            s2_freq[s2[right-len(s1)]]-=1
            if s2_freq[s2[right-len(s1)]]==0:
                s2_freq.pop(s2[right-len(s1)])
            if s1_freq==s2_freq:
                return True
        return False
            
            