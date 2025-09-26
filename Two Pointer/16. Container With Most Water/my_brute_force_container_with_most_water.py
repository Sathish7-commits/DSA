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
        # Time complexity: O(n²)
        # Space complexity: O(n²)
        # iterate through the list using for loop
        # use while loop to iterate through each combination
        # subtract the index of the for loop and the while loop's index
        # multiply that with the min(both values) and store that in a list
        # iterate through all and finally return the maximum of the list
        all_capacity = []
        for i in range(len(heights)):
            left = i+1
            right = len(heights)-1
            while left <= right:
                width = abs(left-i)
                height = min(heights[i], heights[left])
                capacity = width * height
                all_capacity.append(capacity)
                left += 1

        return max(all_capacity)


sln = Solution()
output = sln.maxArea(heights=[1,7,2,5,4,7,3,6])
print(output)


