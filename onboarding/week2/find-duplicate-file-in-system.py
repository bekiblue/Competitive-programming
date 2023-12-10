from collections import defaultdict 
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_paths=defaultdict(list)
        for directory in paths:
            path,*files=directory.split()
            for file in files:
                start=file.find("(")
                file_name=file[:start]
                content=file[start+1:len(file)-1]
                content_paths[content].append(path+"/"+file_name)
        answer=[]
        for content_path in content_paths.values():
            if len(content_path)>1:
                answer.append(content_path)
        return answer