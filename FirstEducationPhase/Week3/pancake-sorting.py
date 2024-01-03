class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
            answer=[]
            for position in range(len(arr)-1,0,-1):
                mxm=position
                for index in range(position):
                    if arr[index] > arr[mxm]:
                        mxm=index
                if mxm != position:
                    answer.append(mxm+1)
                    arr=arr[:mxm+1][::-1]+arr[mxm+1:]
                    answer.append(position+1)
                    arr=arr[:position+1][::-1]+arr[position+1:]            
            return answer
                
