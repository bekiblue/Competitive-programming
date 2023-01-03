#User function Template for python3
#User function Template for python3

class Solution: 
    def select(self, arr, i):
        self.min=arr[i]
        self.index=i
        for j in range(n-i-1):
            temp=j+i+1
            if arr[temp] < self.min :
                self.min=arr[temp]
                self.index=temp
        return self.min,self.index
    
    def selectionSort(self, arr,n):
        for i in range(n):
            self.min,self.index=self.select(arr,i)
            del arr[self.index]
            arr.insert(i,self.min)


            
            

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
