class Solution:
    def row(self,char):
        if char in "qwertyuiop":
            return 1
        elif char in "asdfghjkl":
            return 2
        else:
            return 3
    def findWords(self, words: List[str]) -> List[str]:
        answer=[]
        for word in words:
            for char in range(len(word)):
                if char < len(word)-1 and self.row(word[char].lower()) != self.row(word[char+1].lower()):
                    break 
            else:
                answer.append(word)
        return answer
