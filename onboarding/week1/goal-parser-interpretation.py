class Solution:
    def interpret(self, command: str) -> str:
        answer=""
        index=0
        while index<len(command):
            if index==len(command)-1 and command[index]=="G":
                answer+="G"
                break
            if command[index]=="G":
                answer+="G"
                index+=1
            elif command[index]=="(" and command[index+1]==")":
                answer+="o"
                index+=2
            else:
                answer+="al"
                index+=4
        return answer
            

        