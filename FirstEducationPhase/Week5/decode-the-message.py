class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decoder={}
        asci=97
        for char in key:
            if char != " " and char  not in decoder :
                decoder[char]=chr(asci)
                asci+=1
        decoder[" "]=" "
        decoded=""
        for char in message:
            decoded+=decoder[char]
        return decoded
            


            