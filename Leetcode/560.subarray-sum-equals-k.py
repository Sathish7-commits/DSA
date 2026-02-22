#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from typing import List
class Solution:
    '''
    Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Example 1:

        Input: nums = [1,1,1], k = 2
        Output: 2
    
    Example 2:
        
        Input: nums = [1,2,3], k = 3
        Output: 2
 

    Constraints:

        1 <= nums.length <= 2 * 104
        -1000 <= nums[i] <= 1000
        -107 <= k <= 107
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        frequency = {0:1}

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in frequency:
                count += frequency[prefix_sum-k]

            frequency[prefix_sum] = frequency.get(prefix_sum,0)+1
        return count

                


# @lc code=end