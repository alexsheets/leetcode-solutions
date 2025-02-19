# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

#--------------------------------------------------------------------------------------------------------------------

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hm = {}

        for i in range(0, len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 1
            else:
                hm[nums[i]] += 1
        
        for num, value in hm.items():
            if value == 1:
                return num
            

# EXPLANATION AND COMPLEXITY:
# uses O(n) runtime complexity as we only have to loop through the list and view each element once max
# and accessing and using the hashmap is done in O(1) time. we also use the same amount of memory with one hashmap 
# which is constant regardless of n.
# my immediate thought in this case was to use a hashmap because it is the easiest to keep track of k/v pairs and increment them
# then check afterwards for the key where value = 1