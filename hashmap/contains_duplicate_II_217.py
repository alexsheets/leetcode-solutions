# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

#-----------------------------------------------------------------------------------------------------------------------------------------


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # move through array once and store positions for each key in the hash
        # once we meet a key we have seen before check the absolute distance between
        # the current index and the past index
        # if <= k return true, else add to hashmap

        hm = {}

        for i, num in enumerate(nums):
            if num in hm and abs(i - hm[num]) <= k:
                return True
            else:
                hm[num] = i

        return False        
    

# EXPLANATION AND COMPLEXITY:
# uses O(N) complexity as we only have to progress through the list once
# utilizes hashmap to keep key and value for each digit and its position and then calculates the difference in said positions once it meets a duplicate