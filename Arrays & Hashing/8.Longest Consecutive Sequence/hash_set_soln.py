class Solution:
	"""
	Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

	A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

	You must write an algorithm that runs in O(n) time.

	Example 1:

	Input: nums = [2,20,4,10,3,4,5]

	Output: 4
	Explanation: The longest consecutive sequence is [2, 3, 4, 5].

	Example 2:

	Input: nums = [0,3,2,5,4,6,1,1]

	Output: 7
	Constraints:

	0 <= nums.length <= 1000
	-10^9 <= nums[i] <= 10^9
	"""
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if (num-1) not in numset: # Start only at the start of sequence. for [4,2,3] start only when it comes to 2 and avoid the core logic when at 4 or 3
                length = 1
                while num+length in numset:
                    length+=1
                longest = max(longest, length) # to capture the maximum seq. when there are two or more seq like 2,3,4 and 45,46,47,48
        return longest