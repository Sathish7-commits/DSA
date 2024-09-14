class Solution:
  """
  Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
  Each product is guaranteed to fit in a 32-bit integer.
  Follow-up: Could you solve it in O(n) time without using the division operation?

  Example 1:
    Input: nums = [1,2,4,6]
    Output: [48,24,12,8]
  
  Example 2:
    Input: nums = [-1,0,1,2,3]
    Output: [0,-6,0,0,0]
  """
  
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_list = []

        for i in range(len(nums)):
            removed_element = nums.pop(i)
            output_list.append(eval(' * '.join(map(str, nums))))
            nums.insert(i,removed_element) 
            
        return output_list
