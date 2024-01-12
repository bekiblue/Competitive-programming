class Solution:
    def balancedString(self, s: str) -> int:
        # for each character count the extra apperances than n/4
        # then find the a minimum length subarray that contains letters having at least the extra apperances in the subarray for each character
        freq=defaultdict(int)
        for char in s:
            freq[char]+=1
        extra_W=freq["W"]-len(s)//4 if freq["W"] > len(s)//4 else 0
        extra_Q=freq["Q"]-len(s)//4 if freq["Q"] > len(s)//4 else 0
        extra_E=freq["E"]-len(s)//4 if freq["E"] > len(s)//4 else 0
        extra_R=freq["R"]-len(s)//4 if freq["R"] > len(s)//4 else 0
        if extra_W==extra_Q==extra_E==extra_R==0:
            #if there are no extra appearances it's balanced
            return 0
        mnm=len(s)
        window_freq=defaultdict(int)
        left=0
        for right in range(len(s)):
            window_freq[s[right]]+=1
            while  window_freq["Q"] >= extra_Q and window_freq["W"] >= extra_W and window_freq["E"] >= extra_E and window_freq["R"] >= extra_R:
                mnm=min(mnm,right-left+1)
                window_freq[s[left]]-=1
                left+=1
        return mnm



        

