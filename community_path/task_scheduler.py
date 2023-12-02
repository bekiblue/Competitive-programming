class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        most_freq = freq.most_common()[0][1]
        found_most = sum([freq[key] == most_freq for key in freq])
        return max(len(tasks), (most_freq - 1) * (n+1) + found_most)
