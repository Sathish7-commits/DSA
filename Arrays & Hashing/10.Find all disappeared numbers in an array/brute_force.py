class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums) + 1
        not_present = []
 
        for num in range(1, length):
            if num not in nums:
                not_present.append(num)
        return not_present
