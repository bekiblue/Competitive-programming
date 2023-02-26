class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        place = []
        for n, start, end in trips:
            place.append((start, n))
            place.append((end, -n))
        place.sort()
        pas = 0
        for tup in place:
            pas += tup[1]
            if pas > capacity:
                return False
        return True
