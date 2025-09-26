from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterate through the list using for loop and use while loop to compare against each element
        # store the value of max profit for coint bought on each day
        # return the max profit
        n = len(prices)
        max_profit = 0
        for i in range(n):
            j = i+1
            while j < n:
                max_profit = max(max_profit, prices[j] - prices[i])
                j+=1
        return max_profit

sln = Solution()
output = sln.maxProfit([7,1,5,3,6,4])
print(output)