class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        vector_list = (length + 1) * [-1]

        for num in nums:
            vector_list[num] = num
        
        for index in range(len(vector_list)):
            if vector_list[index] == -1:
                return index
            
        
