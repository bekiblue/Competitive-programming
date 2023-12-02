class Solution:
    def xorQueries(self, arr, queries):
        prefix_xor = [0]*len(arr)
        prefix_xor[0] = arr[0]
        
        for i in range(1, len(prefix_xor)):
            prefix_xor[i] = prefix_xor[i-1] ^ arr[i]
        
        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(prefix_xor[r])
                continue
            
            ans.append(prefix_xor[l-1] ^ prefix_xor[r])
        
        return ans
