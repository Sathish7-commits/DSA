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
        # prefix sum method maintains a running total and subtracting from k shows us if the element is present in the array
        '''
        # nums = [7,4,3,2,1,3,5,6], k = 1
        i=0 → 7

        prefix_sum = 7
        Need 7-1 = 6 → not in freq
        freq = {0:1, 7:1}

        i=1 → 4

        prefix_sum = 11
        Need 11-1 = 10 → not in freq
        freq = {0:1,7:1,11:1}

        i=2 → 3

        prefix_sum = 14
        Need 14-1 = 13 → not found
        freq add 14

        i=3 → 2

        prefix_sum = 16
        Need 16-1 = 15 → not found
        freq add 16

        i=4 → 1

        prefix_sum = 17
        Need 17-1 = 16

        Is 16 in freq?
        Yes.

        So:

        count += freq[16]
        freq[16] = 1

        count = 1
        '''
        prefix_sum = 0
        count = 0
        frequency = {0:1}

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in frequency: # prefix_sum - k -> actually helps checks the sum between subarray
                count += frequency[prefix_sum-k]

            frequency[prefix_sum] = frequency.get(prefix_sum,0)+1
        return count

                


# @lc code=end