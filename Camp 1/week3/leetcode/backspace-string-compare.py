class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_written=[]
        t_written=[]
        for char in s:
            if char=="#":
                if s_written:
                    s_written.pop()
            else:
                s_written.append(char)
        for char in t:
            if char=="#":
                if t_written:
                    t_written.pop()
            else:
                t_written.append(char)
        return s_written==t_written