from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize variables
        n = len(temperatures)  # Number of temperatures
        result = [0] * n       # Initialize result array with zeros
        stack = []             # Stack to store indices of temperatures

        # Iterate through the temperatures
        for i in range(n):
            # Check if the current temperature is higher than the temperature at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # If yes, update result for the previous index and pop it from the stack
                prev_index = stack.pop()
                result[prev_index] = i - prev_index

            # Add the current index to the stack
            stack.append(i)

        return result






'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        oneSidePeaks = [0]

        for i in range(1,len(temperatures)):
            oneSidePeaks.append(1 if temperatures[i] > temperatures[i-1] else 0)
        print(oneSidePeaks)


        for i in range(len(oneSidePeaks)-1):
            j = i + 1
            c = 1

            while j < len(oneSidePeaks)-1:
                if oneSidePeaks[j] == 1:
                    if temperatures[j] >= temperatures[i]:
                        break
                
                c+=1
                j+=1

            oneSidePeaks[i] = c


        print(oneSidePeaks)

        return oneSidePeaks

'''

