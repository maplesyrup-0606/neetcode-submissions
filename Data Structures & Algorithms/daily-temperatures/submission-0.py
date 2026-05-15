class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret =[0 for _ in range(n)]

        stack = [(temperatures[0], 0)]
        for i in range(1, n):
            new_temp = (temperatures[i], i)

            while True:
                if stack: 
                    prev_temp = stack.pop()

                    if prev_temp[0] >= new_temp[0]:
                        stack.append(prev_temp)
                        break
                    else:
                        ret[prev_temp[1]] = new_temp[1] - prev_temp[1]
                else:
                    break
            stack.append(new_temp)
    
        return ret