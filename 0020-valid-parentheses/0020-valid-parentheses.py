class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of open brackets
        stack = []
        
        # Dictionary to store the mapping of open and close brackets
        Brackets = {"(": ")", 
                    "[": "]",
                    "{": "}"}

        # Iterate through each character in the input string
        for char in s:
            # If the character is an open bracket, push it onto the stack
            if char in Brackets.keys():
                stack.append(char)
            
            # If the character is a closing bracket and matches the corresponding open bracket
            elif stack and char == Brackets[stack[-1]]:
                # Pop the matching open bracket from the stack
                stack.pop(-1)
                
            # If the character is a closing bracket, but there is no matching open bracket on the stack
            else:
                # The string is not valid
                return False

        # After processing all characters, check if the stack is empty
        # If not, there are unmatched open brackets, and the string is not valid
        if stack:
            return False 
        # If the stack is empty, all brackets have been matched, and the string is valid
        return True
