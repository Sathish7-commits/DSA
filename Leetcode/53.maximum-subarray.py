#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if sum is hurting the momentum, drop it and restart
        currentsum = 0
        maxsum = float(-inf)
        for num in nums:
            currentsum = max(num, currentsum+num)
            maxsum = max(currentsum, maxsum)
        return maxsum
# @lc code=end