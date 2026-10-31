class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        
        # store the temp which haven't meet the warmer day
        stack = []

        for i in range(n):
            cur_tmp = temperatures[i]

            # compare cur_tmp with prev_tmp(temperature[stack.pop()])
            while stack and cur_tmp>temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i-prev_index

            # add current tmp index into stack        
            stack.append(i)

        return result
