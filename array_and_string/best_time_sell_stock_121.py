# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#-------------------------------------------------------------------------------------------------------------------------------------------------


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestNum = 10000
        largestMargin = 0
        # look at each element in array
        for i in range(len(prices)):
            # if the current price is less than lowest number we've seen
            if (prices[i] < lowestNum):
                # reassign the lowest number as this one
                lowestNum = prices[i]
            # otherwise, if it is actually more than we currently have as lowest number
            else:
                # figure out price margin between current element and lowest number we have seen
                margin = prices[i] - lowestNum
                if (margin > largestMargin):
                    largestMargin = margin

        return largestMargin
    
# COMPLEXITY/SOLUTION EXAMPLE: O(N). we simply travel through the prices array linearly and do primitive checks and operations.
# during the linear travel, we view each element, decide if it is the lowest we've seen; if it is, then assign this number as the lowest we've seen.
# if it isn't, then we simply want to find the margin between the current price we're at and the lowest which came prior.
# we can use a precreated variable to hold the largest margin we've found to easily compare once we calculate each margin, then return the largest we finish with
