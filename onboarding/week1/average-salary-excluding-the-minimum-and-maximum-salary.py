class Solution:
    def average(self, salary: List[int]) -> float:
        mnm=min(salary[0],salary[1])
        mxm=max(salary[0],salary[1])
        total=0
        for employee in salary[2:]:
            if employee<mnm :
                total+=mnm   
                mnm=employee
            elif employee>mxm :
                total+=mxm
                mxm=employee
            else:
                total+=employee
        return total/(len(salary)-2)


