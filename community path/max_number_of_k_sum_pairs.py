class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        map = {}
        count = 0
        for num in nums:
            res = k - num
            if res in map:
                count += 1
                if map.get(res) == 1: del map[res]
                else: map.update({res : map.get(res) - 1})
            else:
                map[num] = map.get(num, 0) + 1
        return count
