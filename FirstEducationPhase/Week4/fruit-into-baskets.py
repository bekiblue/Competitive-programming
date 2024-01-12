class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # find the maximum length of the subarray that contains at most two distinict fruit types
        mxm=0
        type1_last_index=-1
        type2_last_index=-1
        left=0
        for right in range(len(fruits)):
            if type1_last_index==-1 or fruits[right] == type1:
                type1_last_index=right
                type1=fruits[right]
            elif type2_last_index==-1  or fruits[right] == type2:
                type2_last_index=right
                type2=fruits[right]
            else:
                if type1_last_index < type2_last_index:
                    left=type1_last_index+1
                    type1_last_index=right
                    type1=fruits[right]
                else:
                    left=type2_last_index+1
                    type2_last_index=right
                    type2=fruits[right]
            mxm=max(mxm,right-left+1)
        return mxm