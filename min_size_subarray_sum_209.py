# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

#----------------------------------------------------------------------------------------------------

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        least = 0
        curr = 0
        i = 0
        for j in range(len(nums)):
            curr += nums[j]
            while curr >= target:
                if least == 0:
                    least = j-i+1
                else:
                    least = min(least, j-i+1)
                curr -= nums[i]
                i += 1
        
        return least
    
# EXPLANATION AND COMPLEXITY:
# uses O(n) time complexity and O(1) space complexity as we do not have to allocate any extra space besides 
# variables and only has to traverse the array of numbers at most once to find its solutions
# initially, i had a more brute force solution and was forced to change it due to time limits on execution.
# this led me to find a more pacey solution which simply uses two pointers in a sliding window form