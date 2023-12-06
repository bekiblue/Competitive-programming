class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mxm=max(candies)
        result=[]
        for kid in range(len(candies)):
            if candies[kid]+extraCandies >= mxm:
                result.append(True)
            else:
                result.append(False)
        return result