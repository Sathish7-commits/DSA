class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_list = 0

        # Adding 1 coz we are including 0 in the given list. Count just the number of elements given for 'n'

        actual_length = len(nums) + 1

        for index in range(actual_length):
            xor_list = xor_list ^ index 
        
        for num in nums:
            xor_list = xor_list ^ num
        
        return xor_list
