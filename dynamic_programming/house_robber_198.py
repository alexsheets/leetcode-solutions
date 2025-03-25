# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that 
# adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        # create array to store max rob 
        maxRob = [0] * len(nums)
        # instantiate first and second positions (array at least 2 elements)
        maxRob[0] = nums[0]
        maxRob[1] = max(nums[0], nums[1])

        # for each index beyond first 2, get max of either previous rob total or its previous adjacent element plus the new el
        for ind in range(2, len(nums)):
            maxRob[ind] = max(maxRob[ind-1], maxRob[ind-2] + nums[ind])

        # last el stores largest value
        return maxRob[-1]
    


# EXPLANATION AND COMPLEXITY:
# uses O(n) time and space. only keeps one array of extra space to keep track of solution.
# my first solutions had gotten long and messy with chains of if/else at which point i realized the solution must be more simple
# writing the problem out and realizing a good pattern was crucial to figuring out this dynamic programming problem.
# the most crucial part of this algorithm is taking the max between robbing the current house or skipping it for each entry in the soln array