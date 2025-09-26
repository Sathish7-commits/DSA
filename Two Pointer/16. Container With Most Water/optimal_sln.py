from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        You are given an integer array heights where heights[i] represents the height of the ith bar.

        You may choose any two bars to form a container. Return the maximum amount of water a container can store.

        Example 1:
            Input: height = [1,7,2,5,4,7,3,6]
            Output: 36

        Example 2:
            Input: height = [2,2,2]
            Output: 4
        """
        left = 0
        right = len(heights) - 1
        max_capacity = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            max_capacity = max(max_capacity, width * height)

            if heights[left] < heights[right]:
                left +=1
            else:
                right -= 1

        return max_capacity


sln = Solution()
output = sln.maxArea(heights=[1,7,2,5,4,7,3,6])
print(output)
