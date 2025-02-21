# Given an integer array nums of unique elements, return all possible subsets
# The solution set must not contain duplicate subsets. Return the solution in any order.
#---------------------------------------------------------------------

class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     list_of_lists = []
    #     list_of_lists.append([])
    #     self.subset_recurse(nums, list_of_lists)
    #     return list_of_lists

    # def subset_recurse(self, nums, result):
    #     n = len(nums)
    #     result.append([nums[0]])
    #     final_list = [nums[0]]

    #     if (n == 1):
    #         return

    #     # append new list which has first 
    #     for i in range(1, n):
    #         new_list = [nums[0], nums[i]]
    #         final_list.append(nums[i])
    #         result.append(new_list)
        
    #     if final_list not in result:
    #         result.append(final_list)
    #     self.subset_recurse(nums[1:], result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        soln = []

        def backtrack(i):
            # append copy of solution if at leaf node
            if i == n:
                result.append(soln[:])
                return
            
            # backtrack next index (not picking up current)
            backtrack(i+1)
            # after this, also take path of picking current
            soln.append(nums[i])
            # deal with our choice
            backtrack(i+1)
            # pop same number we just appended
            soln.pop()

        # start backtracking at beginning
        backtrack(0)
        return result
    


# EXPLANATION AND COMPLEXITY:
# uses O(2^n) running time. at each level of subsets generated, the running time necessary/calls made use 2^length of list time.
# as for the solution, i left my initial one in the code. my original answer only generated subsets which did not also work backward
# and include all subsets. then i realized i would need some sort of backtracking solution, which required me to draw out the problem 
# and code more accordingly to the problem itself.