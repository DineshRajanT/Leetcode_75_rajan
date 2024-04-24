# class Solution:
#     def calcTribonacci(self, num):
#         if num == 0:
#             return 0
#         elif num == 1 or num == 2:
#             return 1
#         else:
#             return self.calcTribonacci(num-1) + self.calcTribonacci(num-2) + self.calcTribonacci(num-3)

#     def tribonacci(self, n: int) -> int:
#         return self.calcTribonacci(n)

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        # Initialize the first three terms of the Tribonacci sequence
        tribonacci_sequence = [0, 1, 1]

        # Calculate the nth term iteratively
        for i in range(3, n + 1):
            next_term = tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 3]
            tribonacci_sequence.append(next_term)

        return tribonacci_sequence[n]
