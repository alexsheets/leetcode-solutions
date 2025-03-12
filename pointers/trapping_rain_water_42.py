# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


#--------------------------------------------------------------------------------------

class Solution:
    def trap(self, height: List[int]) -> int:
            
        # sliding window
        # if lower, increment front index (add to a counter?)
        # if higher then calculate trapped water then tighten window

        if len(height) == 0:
            return 0
        
        slow = 0
        fast = len(height)-1
        total_sum = 0
        slow_max, fast_max = 0, 0

        while slow < fast:
            # if lower than height of right side of window
            if height[slow] < height[fast]:
                # either change max or calculate difference, then inc
                if height[slow] >= slow_max:
                    slow_max = height[slow]
                else:
                    total_sum += slow_max - height[slow]
                slow += 1
            else:
                # heights are either equal or left side greater
                if height[fast] >= fast_max:
                    fast_max = height[fast]
                else:
                    total_sum += fast_max - height[fast]
                fast -= 1
        
        return total_sum


# EXPLANATION AND COMPLEXITY:
# uses O(n) complexity as we use a sliding window to only process each element once. without using one, this would 
# need to be n^2 complexity as we would have to use nested loops.
# the problem was clearly going to need a sliding window, the implementation however was not the normal one
# where you slide a window of certain length across the initial array; rather the sliding window in this problem
# starts at widest possible then shrinks down to smallest and keeps adding the 'trapped water' along the way.