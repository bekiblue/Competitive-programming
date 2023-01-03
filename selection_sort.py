#User function Template for python3


class Solution: 
    def select(self, arr, i):
        self.min=arr[i]
        self.index=i
        for j in range(i+1,len(arr)):
            if arr[j] < self.min :
                self.min=arr[j]
                self.index=j
        return self.index
    
    def selectionSort(self, arr,n):
        for i in range(n):
            self.index=self.select(arr,i)
            arr[i],arr[self.index]=arr[self.index],arr[i]
            
            



            
            

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
