class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        decreasing=[]
        next_greater=defaultdict(lambda :-1)
        for index,num in enumerate(nums2):
            while decreasing and num > nums2[decreasing[-1]]: # Top of the stack
                # Save the next greater of the top element in the map to be num
                popped=nums2[decreasing.pop()] 
                next_greater[popped]=num
            # Push the index to the decreasing stack
            decreasing.append(index)
        answer=[ next_greater[num] for num in nums1]
        return answer         