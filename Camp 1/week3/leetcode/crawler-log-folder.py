class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dirs=[]
        for log in logs:
            if log=="./":
                continue
            elif log =="../":
                if dirs:
                    dirs.pop()
            else:
                dirs.append(log)
        return len(dirs)