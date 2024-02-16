class Solution:
    def simplifyPath(self, path: str) -> str:
        modified=[]
        directories=path.split("/")
        for directory in directories:
            if not directory or directory == ".":
                continue
            elif directory=="..":
                if modified:
                    modified.pop()
                else:
                    continue
            else:
                modified.append(directory)
        return "/"+"/".join(modified)

            
                
            
            
                

                



