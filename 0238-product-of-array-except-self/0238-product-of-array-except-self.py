class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize an array to store the results
        resArr = [1] * len(nums)
        
        # Initialize variables to keep track of prefix and postfix products
        prefix, postfix = 1, 1

        # Calculate prefix products
        for i in range(len(nums)):
            resArr[i] = prefix  # Store the prefix product at the current index
            prefix = prefix * nums[i]  # Update the prefix product for the next iteration

        # Print the intermediate result
        print(resArr)
        
        # Calculate postfix products and multiply them with prefix products
        for i in range(len(nums)-1, -1, -1):
            resArr[i] = resArr[i] * postfix  # Multiply the prefix product with the postfix product
            postfix = postfix * nums[i]  # Update the postfix product for the next iteration

        # Print the final result
        print(resArr)
    
        return resArr
