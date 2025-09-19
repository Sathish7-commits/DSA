from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # store the result in a list
        # use for loop to iterate the list
        # edge case: [0,0,0,0] -> to return [[0,0,0]] we need to allow first time, next iterations have to be skipped
        # use while loop and control variables as left and right
        # increment left and right if it is the same value as that of the current value
        # return the list

        triplets = []
        nums = sorted(nums)
        length_of_nums = len(nums)

        for i in range(length_of_nums-2):
            left = i+1
            right = length_of_nums - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    triplets.append([nums[i],nums[left],nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left+=1
                    right-=1

                elif total < 0:
                    left+=1

                else:
                   right-=1

        return triplets


sln = Solution()
# output = sln.threeSum([-1,0,1,2,-1,-4])
# output = sln.threeSum([0,0,0,0])
output = sln.threeSum([3,0,-2,-1,1,2])
print(output)
