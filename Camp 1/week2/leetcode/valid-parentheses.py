class Solution:
    def isValid(self, s: str) -> bool:
        braces={")":"(","}":"{","]":"["}
        opened=[]
        for char in s:
            if char in braces:
                if opened and braces[char]==opened[-1]:
                    opened.pop()
                    continue
                else:
                    return False
            opened.append(char)
        return True if not opened else False
        
                
                
