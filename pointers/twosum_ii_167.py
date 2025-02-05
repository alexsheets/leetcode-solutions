# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

#---------------------------------------------------------------------------------------------------------------------------------------


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        slow = 0
        fast = len(numbers)-1

        while slow < fast:
            total = numbers[slow] + numbers[fast]
            if total == target:
                return [slow+1, fast+1]
            elif total < target:
                slow += 1
            else:
                fast -= 1


# EXPLANATION AND COMPLEXITY:
# uses O(n) time complexity as we only loop through array once and O(1) space complexity as we do not need extra space regardless of input size
# could be improved by using a binary search possibly, but the immediate answer which came to mind was to use two pointers