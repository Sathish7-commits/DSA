class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_list = 0

        for num in nums:
            xor_list = xor_list ^ num
        
        return xor_list
