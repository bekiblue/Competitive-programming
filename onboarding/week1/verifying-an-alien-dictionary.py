class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordering = {}
        for index, val in enumerate(order):
            ordering[val] = index
        for word in range(len(words)-1):
            for index in range(len(words[word])):
                if index == len(words[word+1]):
                     return False
                if words[word][index] == words[word+1][index]:
                    continue
                elif ordering[words[word][index]] < ordering[words[word+1][index]]:
                    break
                else:
                    return False
        return True
   

        
