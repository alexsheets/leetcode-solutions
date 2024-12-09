# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

#----------------------------------------------------------------------------------------------------

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        kMaxValues = []

        # for each index in length of arr
        for i in range(len(nums)):
            # if the key (number) is in hashmap
            if nums[i] in hm:
                # then add to its value (iterator)
                hm[nums[i]] += 1
            else:
                # else, the amount of times we have seen this key is 1
                hm[nums[i]] = 1
        
        # create array of length hashmap (ie keys we have seen)
        a = [0] * (len(hm))
        j = 0
        # for each key in our hashmap
        for i in hm:
            # set array at jth position to be the key and value
            a[j] = [i, hm[i]]
            j += 1
        
        # use python package to sort the keys in reverse
        a = sorted(a, key=lambda x: x[0], reverse=True)
        # then sort the values in reverse
        a = sorted(a, key=lambda x: x[1], reverse=True)

        # for each index in our array up to k append the key
        for i in range(k):
            kMaxValues.append(a[i][0])

        return kMaxValues
    

## COMPLEXITY: O(n log n) --> n being the size of the array to be sorted and log N being an average number of comparisons we need to place it in the right index
## utilizes hashmap for faster lookup and maintenance