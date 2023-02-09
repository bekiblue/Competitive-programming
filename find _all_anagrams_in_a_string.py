class Solution:
    def findAnagrams(self, s: str, p: str):        
        result = list()
        left, right = 0, len(p)-1
        s_count, p_count = Counter(s[0:len(p)]), Counter(p)
        
        while True:
            if not len(p_count - s_count):
                result.append(left)
            
            if s[left] in s_count: 
                s_count[s[left]] -= 1
            right, left = right+1, left+1

            if right >= len(s):
                break
                
            s_count[s[right]] += 1 
        
        return result
            
