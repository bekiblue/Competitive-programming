
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        answer = 0
        l = 0
        r = k-1
        cur_sum = sum(arr[0:k-1])
        while r < len(arr):
            cur_sum += arr[r]
            if cur_sum / k >= threshold:
                answer += 1
            cur_sum -= arr[l]
            l += 1
            r += 1
        
        return answer
