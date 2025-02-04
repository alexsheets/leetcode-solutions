# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

#------------------------------------------------------------------------------------------------------------------

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i=0
        j=0

        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        return i == len(s)
    

# EXPLANATION AND COMPLEXITY:
# uses O(n) time complexity and is a pretty simple problem.
# use an outer loop to loop through the longer sequence and then loop through
# the given subsequence and iterate i where we find a matching char for our subsequence