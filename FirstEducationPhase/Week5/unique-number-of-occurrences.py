class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq=Counter(arr)
        occurrences=set()
        for num in freq:
            if freq[num] in occurrences:
                return False 
            occurrences.add(freq[num])
        return True