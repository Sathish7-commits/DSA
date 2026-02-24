#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    '''
    Given an integer array nums, find a subarray that has the largest product, and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.

    Note that the product of an array with a single element is the value of that element.

    Example 1:

        Input: nums = [2,3,-2,4]
        Output: 6
        Explanation: [2,3] has the largest product 6.
    
    Example 2:
    
        Input: nums = [-2,0,-1]
        Output: 0
        Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
    
    Constraints:

    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
    '''
    from typing import List
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        current_max = 1
        current_min = 1

        for num in nums:
            if num == 0:
                current_max, current_min = 1,1
                continue
            
            temp_max = num * current_max
            current_max = max(num * current_max, num * current_min, num)
            current_min = min(temp_max, num * current_min, num)
            result = max(result, current_max)
        return result

soln = Solution()
result = soln.maxProduct(nums=[2,3,-2,4])
print(result)
# @lc code=end
