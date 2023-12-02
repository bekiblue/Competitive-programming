class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len=max(len(word1),len(word2))
        s=""
        for index in range(max_len):
            if index<len(word1):
                s+=word1[index]
            if index<len(word2):
                s+=word2[index]
        return s