class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # Define supported operators
        OPERATORS = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: int(x / y)}

        # Initialize an empty stack
        stack = []

        # Iterate through every token in the given expression
        for token in tokens:
            # Check if the current token is an operator
            if token in OPERATORS:
                # Pop out the top two numbers from the stack
                num_two, num_one = stack.pop(), stack.pop()

                # Perform the corresponding operation on the popped numbers
                result = OPERATORS[token](num_one, num_two)

                # Push the calculated result back onto the stack
                stack.append(result)
            else:  
                # Treat the current token as an integer operand and add it to the stack
                stack.append(int(token))

        # Return the final result stored on the stack
        return stack[-1]