class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1=0
        p2=0
        answer=[]
        while p1<len(firstList) and p2 < len(secondList):
            if firstList[p1][0] <= secondList[p2][0]:
                if  firstList[p1][1] >= secondList[p2][0]:
                    if secondList[p2][1] <= firstList[p1][1]:
                        answer.append(secondList[p2])
                        p2+=1
                    else:
                        answer.append([secondList[p2][0],firstList[p1][1]])
                        p1+=1
                else:
                    p1+=1
            else:
                if secondList[p2][1]>=firstList[p1][0]:
                    if firstList[p1][1] <= secondList[p2][1] :
                        answer.append(firstList[p1])
                        p1+=1
                    else:
                        answer.append([firstList[p1][0],secondList[p2][1]])
                        p2+=1
                else:
                    p2+=1
        return answer