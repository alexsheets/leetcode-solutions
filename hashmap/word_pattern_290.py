# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

#------------------------------------------------------------------------------------------------------------------

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # for each letter in the original string
        # start mapping to a hashmap and once we get that key again
        # if the value we have from other string is not equal
        # then return false

        hm = {}
        tracker = 0
        newStr = s.split(" ")

        if len(newStr) != len(pattern):
            return False

        for word in newStr:
            char = pattern[tracker]
            if char not in hm:
                if word not in hm.values():
                    hm[char] = word
                else:
                    return False
            else:
                # we have already seen this character so the word should 
                # be equal to its value
                if (hm[char] != word):
                    return False
            
            tracker += 1
        
        return True
    

# EXPLANATION AND COMPLEXITY:
# 