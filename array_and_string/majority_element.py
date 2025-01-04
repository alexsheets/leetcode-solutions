# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

#-----------------------------------------------------------------------------

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hm = {}

        if len(nums) == 0:
            return 0
        elif len(nums)==1:
            return nums[0]

        for i in range(0, len(nums)):
            if nums[i] in hm:
                hm[nums[i]] += 1
            else:
                hm[nums[i]] = 1

        return max(hm, key=hm.get)


# EXPLANATION AND COMPLEXITY:
# uses O(N) time and space complexity as each element only has to be visited once then we perform
# an O(1) hashmap check to get the key of the max value 
# the solution was simple to come up with if you know how hashmaps work. you can simply visit each
# element while incrementing the key associated with it