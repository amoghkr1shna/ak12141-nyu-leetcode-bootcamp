class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures) # no. of days
        answer = [0] *n
        s = []

        for curr_day, curr_temp in enumerate(temperatures): #day is index and temp is data
            while s and temperatures[s[-1]] < curr_temp: #if stack isn't empty and current temperature's 
                                                        #greater than the temp on the day at the ToS
                prev_day = s.pop() #pop the warmer day
                answer[prev_day] = curr_day - prev_day #get the no. of days between the 2 days
            s.append(curr_day)
        
        return answer

