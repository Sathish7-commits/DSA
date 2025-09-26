from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Given an array of integers numbers that is sorted in non-decreasing order.
        Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
        There will always be exactly one valid solution.

        Your solution must use O(1) additional space.

        Example 1:
        Input: numbers = [1,2,3,4], target = 3
        Output: [1,2]

        Explanation:
        The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].
        """
        # numbers should add up to target
        # return the indices in a list
        # don't use a list to store that
        # use two pointer approach
        # iterate from both left and right
        # if left+right < target then left+1
        # else right-1
        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left+=1
            else:
                right-=1


sln = Solution()
output = sln.twoSum(numbers=[1,2,3,4],target=3)
print(output)