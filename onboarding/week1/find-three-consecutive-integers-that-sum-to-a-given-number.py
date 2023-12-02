class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3 == 0 :
            return [(num-3)//3,((num-3)//3)+1,((num-3)//3)+2]
        return []