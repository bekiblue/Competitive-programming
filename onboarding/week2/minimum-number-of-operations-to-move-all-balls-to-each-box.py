class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        non_empty=[]
        for box in range(len(boxes)):
            if boxes[box]=="1":
                non_empty.append(box)
        answer=[]
        for box in range(len(boxes)):
            answer.append(0)
            for b in non_empty:
                if box != b:
                    answer[-1]+=abs(box-b)
        return answer


