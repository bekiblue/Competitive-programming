class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1]:
            return False
        increasing=True
        for index in range(len(arr)-1):
            if arr[index]==arr[index+1]:
                return False
            elif increasing and arr[index] > arr[index+1]:
                increasing=False
            elif not increasing and arr[index] < arr[index+1]:
                return False
        return True if not increasing else False
        