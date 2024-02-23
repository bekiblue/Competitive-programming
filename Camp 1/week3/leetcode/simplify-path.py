class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs=[]
        directories=path.split('/')
        for directory in directories :
            if not directory or directory==".":
                continue
            elif directory=="..":
                if dirs:
                    dirs.pop()
            else:
                dirs.append(directory)
        return "/"+"/".join(dirs)
