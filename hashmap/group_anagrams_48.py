# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#----------------------------------------------------------------

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # hold each distinct anagram group
        hm = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hm:
                hm[sorted_word] = [word]
            else:
                hm[sorted_word].append(word)

        lists = [value for key, value in hm.items()]
        return lists
    

# EXPLANATION AND COMPLEXITY:
# this felt like a simple problem because the problem description makes it clear we need some sort
# of distinctive entry point to add each word which is suitable. i decided to simply use the python sort
# package and join the returned array as a string, then check the hashmap and add where it exists or create it.
# at the end simply return the values at each entry in the hashmap. 
# the complexity is O(n * k log k), n is length of strs and k is length of the strings themselves