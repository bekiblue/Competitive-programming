class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dec_temp=[]
        answer=[0]*len(temperatures)
        for index,temp in enumerate(temperatures):
            while dec_temp and temp > temperatures[dec_temp[-1]]: # If it's a warmer temprature than my top temp
                #update the number of days i have to wait 
                popped_temp_index=dec_temp.pop()
                answer[popped_temp_index]=index-popped_temp_index
            dec_temp.append(index)
        return answer
        
