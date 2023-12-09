class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer=""
        prev=0
        for index in range(len(spaces)):
            if index == len(spaces)-1:
                answer+=s[prev:spaces[index]]+" "+s[spaces[index]:]
                return answer
            answer+=s[prev:spaces[index]]+" "
            prev=spaces[index]
