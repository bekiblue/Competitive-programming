class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift=[0]*(len(s)+1)
        for case in shifts:
            if case[2]==1:
                shift[case[0]]+= 1
                shift[case[1]+1]-= 1
            else:
                shift[case[0]]-= 1
                shift[case[1]+1]+= 1

        net_shift=[]
        cur=0
        for i in range(len(s)):
            cur+=shift[i]
            net_shift.append(cur)
        answer=""
        for index,char in enumerate(s):
            new_char=chr(((ord(char)-97+net_shift[index])%26)+97)
            answer+=new_char
        return  answer
        



