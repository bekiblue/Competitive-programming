#User function Template for python3

class Solution: 
    def select(self, arr, i):
        self.min=arr[i]
        for j in arr[i+1:]:
            if j < self.min :
                self.min=j
        return self.min
    
    def selectionSort(self, arr,n):
        for i in range(n):
            sorted_arr=arr[0:i]
            unsorted_arr=arr[i:]
            self.min=self.select(arr,i)
            unsorted_arr.remove(self.min)
            sorted_arr.append(self.min)
            arr=sorted_arr+unsorted_arr
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
