## PROBLEM DEFINITION:
## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
## You may assume that each input would have exactly one solution, and you may not use the same element twice.

#--------------------------------------------------------------------------------------------------------------------------------------

class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store numbers in array using k/v structure
        # number will be key and index in original list is the value
        map = {}
        # iterate through list of numbers and calculate int needed to reach target
        for i, num in enumerate(nums):
            search = target - num
            # if the int has been mapped return indices
            if search in map:
                return [map[search], i]
            # or add current number and index of it in original list to the mapping
            map[num] = i


## COMPLEXITY: constant time, or O(N)
## iterate through list of numbers linearly, target - num runs in constant time
## no nested loop

## SOLUTION EXPLANATION: create hashtable, store as (value, index), traverse through list to find other value/index necessary
