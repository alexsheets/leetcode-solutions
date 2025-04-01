# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

#----------------------------------------------------------------------------------------

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        # get length of array
        # maybe number of each color

        zero_ct = nums.count(0)
        one_ct = nums.count(1)
        two_ct = nums.count(2)

        zeros = 0
        ones = 0
        twos = 0

        for i in range(len(nums)):
            if zeros < zero_ct:
                nums[i] = 0
                zeros += 1
            elif (zeros == zero_ct) and (ones < one_ct):
                nums[i] = 1
                ones += 1
            elif (ones == one_ct) and (twos < two_ct):
                nums[i] = 2
                twos += 1


# can also achieve this solutionusing pointers for low, mid, and high
# start by assigning low, mid to be 0 and high to be len-1

while mid <= high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1
    else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1



# EXPLANATION AND COMPLEXITY:
# my solution ended up being a bit of brute force compared to the most ideal solution, but it is simple in nature and achieves good runtime and memory usage. 
# the problem simply asks us to sort without using the .sort() function. my first thought was to keep a tally of each and then simply rearrange the array according to those numbers

# could also use the counts to do something like
# nums[:R] = [0] * R
# nums[R:R+W] = [1] * W
# nums[R+W:] = [2] * B