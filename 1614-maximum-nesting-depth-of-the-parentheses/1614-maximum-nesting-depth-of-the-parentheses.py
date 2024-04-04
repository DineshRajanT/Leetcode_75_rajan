class Solution:
    def maxDepth(self, s: str) -> int:
        # Initialize an empty stack to keep track of opening parentheses
        stack = []
        # Initialize a variable to keep track of the maximum depth encountered
        globalMax = 0
        # Iterate through each character in the string
        for ch in s:
            # If the current character is an opening parenthesis, '('
            if ch == '(':
                # Push it onto the stack
                stack.append(ch)
                # Update the global maximum depth if the current stack size is greater
                globalMax = max(globalMax, len(stack))
            # If the current character is a closing parenthesis, ')'
            elif ch == ')':
                # Pop an opening parenthesis from the stack (matching with the current closing parenthesis)
                stack.pop()
        
        # Return the maximum depth encountered
        return globalMax
