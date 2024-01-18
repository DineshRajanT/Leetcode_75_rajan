class Solution:
    # Similar to Fibonacci series 
    # n = 5
    # Steps(n):[0, 1, 2, 3, 4, 5]
    # Res   :  [8, 5, 3, 2, 1, 1]

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one

        # arr = [0] * (n+1)
        # arr[n] = 1
        # arr[n-1] = 1
        # for i in reversed(range(n-1)):
        #     arr[i] = arr[i+1] + arr[i+2]
        # print(arr)
        # return arr[0] 

            
        