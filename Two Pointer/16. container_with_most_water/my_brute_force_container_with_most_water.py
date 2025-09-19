from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
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


