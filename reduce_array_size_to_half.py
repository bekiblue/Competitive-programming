class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq_dict={}
        for num in arr:
            if num in freq_dict:
                freq_dict[num]+=1
            else:
                freq_dict[num]=1
        freq=sorted(list(freq_dict.values()),reverse=True)
        count=0
        sum=0
        for i in freq:
            if sum >= len(arr)/2:
                break
            else:
                sum+=i
                count+=1
        return count
        
