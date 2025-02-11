# Given a string s, find the length of the longest substring without repeating characters.

#--------------------------------------------------------------------------------------------------

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        maxLen = 1
        for i in range(0, len(s)-1):
            currStr = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in currStr:
                    currStr += s[j]
                    if len(currStr) > maxLen:
                        maxLen = len(currStr)
                    continue
                else:
                    break

        return maxLen
    

# EXPLANATION AND COMPLEXITY:
# uses O(n*m) complexity, outer loop running in O(n) time and inner loop running in the number of max chars.
# could be improved by using a sliding window, which could then run in O(n) time using pointers to process each character only once
# outside of this, the problem is simple to think of and see how we will find our answer, knowing that we should look at each
# character and generate substring until not possible, then move to the next.