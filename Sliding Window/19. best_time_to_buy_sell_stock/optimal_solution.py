from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit

sln = Solution()
output1 = sln.maxProfit([7,1,5,3,6,4])
output2 = sln.maxProfit([7,6,4,3,1])
print(output1, output2)