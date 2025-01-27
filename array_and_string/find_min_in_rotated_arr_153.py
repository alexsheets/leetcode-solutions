# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

#-------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if (len(nums) == 2):
            return min(nums[0], nums[1])

        # find mid element then conduct binary search
        low = 0
        mid = 0
        high = len(nums) - 1
        x = nums[0]

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] > x:
                low = mid + 1
            elif nums[mid] < x:
                x = nums[mid]
                high = mid - 1
            else:
                return nums[mid]
        
        # if we get here, element we initially had was lowest
        return x
    

# EXPLANATION AND COMPLEXITY: 
# obviously, we are not meant to use the min operator nor meant to simply loop through the array once. the problem states that we should use O log n complexity,
# thus i knew immediately to use a binary search, which halves the array each time we compare an element to the 'middle' element 
# if the number we are comparing to is less than the number we currently hold as the least, then we replace least with said number and half the array
# to look into the half beyond said value. otherwise do the opposite.