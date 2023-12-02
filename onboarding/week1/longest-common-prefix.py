class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for index in range(len(strs[0])):
            char=strs[0][index]
            for word in strs[1:]:
                if index == len(word) or word[index]!=char:
                    return strs[0][:index]
        return strs[0]           
            
                