# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

#----------------------------------------------------------------------------

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # use two pointers to left and right
        # move pointer that points to lower line
        # calculate the amount of water at each step 

        # keep hashmap for results
        hm = {}

        if len(height) == 0:
            return 0
        elif len(height) == 1:
            return height[0]

        left = 0
        right = len(height)-1

        while(left < right):
            
            num = right - left
            minVal = min(height[right], height[left])
            hm[(left, right)] = minVal * num

            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1

        return max(hm.values())

# EXPLANATION AND SOLUTION:
# use a pointer to left and right of array, calculate the water at each step and proceed moving the 'lesser' value
# pointer until finished. in this sense we are able to consider all possibilities without missing
# optimal solution but in such a way that we do not have to over calculate.

# this solution could likely be sped up by finding a simple way to return the largest number without
# keeping them all in a hashmap and finding the max afterward, but it still uses O(N) space complexity
# as each element in the initial array only has to be visited once
