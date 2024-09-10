class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Question:
        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
        Note that you must do this in-place without making a copy of the array.

        Example 1:
          Input: nums = [0,1,0,3,12]
          Output: [1,3,12,0,0]
        
        Example 2:
          Input: nums = [0]
          Output: [0]

        Do not return anything, modify nums in-place instead.
        """
        i = 0 # Tracks the position where the next non-zero element should come
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1 # Next place where the non zero element should go
