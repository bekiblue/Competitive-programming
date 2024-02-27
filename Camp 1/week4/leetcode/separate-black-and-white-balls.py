class Solution:
    def minimumSteps(self, s: str) -> int:
        writer=0
        oper=0
        for reader in range(len(s)):
            if s[reader] == "0":
                oper+=reader-writer
                writer+=1
        return oper

            
            