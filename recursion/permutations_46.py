# Given an array nums of distinct integers, return all the possible permutations

#----------------------------------------------------------------------------------------------

class Solution:

    def recur(self, current, nums, final_list):

        # if we created a new arr of same length as original arr
        # then it should be appended to results
        if len(current) == len(nums):
            final_list.append(current.copy())
            return
        
        # simply look through original array
        for i in nums:
            if i not in current:
                current.append(i)
                self.recur(current, nums, final_list)
                current.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        final_list = []
        self.recur([], nums, final_list)
        return final_list      


# EXPLANATION AND COMPLEXITY:
# uses O(N!) time complexity as at most time we will use the factorial of n time, no more in any case
# the problem was clearly calling for some form of recursion, initially i started by trying to pass the index
# i was analyzing each time but realized that using the array structure to check for validity makes the problem easier