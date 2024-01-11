class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mnm=k
        operations=0
        for index in range(k):
            if blocks[index]=="W":
                operations+=1
        mnm=min(mnm,operations)
        for i in range(k,len(blocks)):
            if blocks[i]=="W":
                operations+=1
            if blocks[i-k]=="W":
                operations-=1
            mnm=min(mnm,operations)
        return mnm
