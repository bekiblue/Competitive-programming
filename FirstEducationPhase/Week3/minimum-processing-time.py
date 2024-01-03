class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        mnm=0
        for group in range(0,len(tasks),4):
            mnm=max(mnm,processorTime[group//4]+tasks[group])
        return mnm

