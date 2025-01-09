# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

#---------------------------------------------------------------------------------------------------------


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # use greedy algorithm to keep track of furthest reachable index

        # initialize variable to hold our max index to reach
        maxJump = 0

        # loop thru array once while viewing index and value of each element
        for i, length in enumerate(nums):
            # if the maxJump when we reach an index is less than the index
            # then we cannot jump to here or beyond, false
            if maxJump < i:
                return False
            # otherwise, the max we can jump is the max of current max jump
            # or the current index plus its element
            maxJump = max(maxJump, i + length)

        # if we reach here without returning false then we made it through arr
        return True
    

# EXPLANATION AND COMPLEXITY:
# this problem was simple, initially i used recursion which passed most of the test cases. then once it had gotten complicated enough, 
# i realized i should take a different approach and implemented a greedy algorithm
# the algorithm is simple in the sense that it loops through the array once making it O(n) and will look at each element while still possible
# to consider whether it is better to take the current value or one we have visited
# once we reach end of array then we know we can return true. if we were not able, it is because the maxJump we have seen before could not reach
# the index we have traversed to.