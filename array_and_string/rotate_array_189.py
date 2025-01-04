class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        # INITIAL INEFFICIENT SOLUTION
        
        # n = 0
        # stack = []
        # while (n <= k):
        #     for i in range(0, len(nums)-1):
        #         if (n == k):
        #             if (stack):
        #                 nums[0] = stack.pop()
        #         else:
        #             curr = nums[i]
        #             if (stack):
        #                 temp = nums[i+1]
        #                 nums[i+1] = stack.pop()
        #                 stack.append(temp)
        #             else:
        #                 next_ = nums[i+1]
        #                 stack.append(next_)
        #                 nums[i+1] = curr
        #     n += 1

        # BETTER SOLUTION

        k %= len(nums)

        # reverse whole arr
        self.reverse(nums, 0, len(nums) - 1)  
        # reverse first k elements
        self.reverse(nums, 0, k - 1)         
        # reverse remaining elements
        self.reverse(nums, k, len(nums) - 1)  

    # reversal algorithm
    def reverse(self, nums, left, right):
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1