# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

#-------------------------------------------------------------------------------------------------------------------------

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # 0,0,1,2,3,4,5,6,7,8

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        nums.sort()
        longestSequence = 1
        hm = {}

        for i in range(len(nums)-1):
            j = i+1
            if ((nums[j] - nums[i]) == 1):
                longestSequence += 1
                if j == len(nums)-1:
                    hm[i] = longestSequence
            elif (nums[j] == nums[i]):
                if j == len(nums)-1:
                    hm[i] = longestSequence
                else:
                    continue
            else:
                hm[i] = longestSequence
                longestSequence = 1

        if len(hm) == 0:
            return 1
        else:
            return max(hm.values())
        

# EXPLANATION AND COMPLEXITY:
# uses O(n log n) time complexity as we utilize a builtin sort which is of O(n log n) complexity and then a hashmap to store our longest sequences
# upon a break in consecutive sequence