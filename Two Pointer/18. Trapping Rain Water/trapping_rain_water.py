from typing import List

class Solution:
    """
    You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

    Return the maximum area of water that can be trapped between the bars.
    https://www.youtube.com/watch?v=KFdHpOlz8hs
    """
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        left_wall = 0
        right_wall = 0

        for i in range(n):
            j = -i - 1

            max_left[i] = left_wall
            max_right[j] = right_wall

            left_wall = max(left_wall, height[i])
            right_wall = max(right_wall, height[j])

        summ = 0
        for i in range(n):
            potential = min(max_left[i], max_right[i])
            summ += max(0, potential - height[i])

        return summ

sln = Solution()
output = sln.trap([0,2,0,3,1,0,1,3,2,1])
print(output)