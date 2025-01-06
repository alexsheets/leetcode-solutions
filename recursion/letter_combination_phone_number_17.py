# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        li = []

        # define recursive function to recursively
        def check(st, digits):
            # if we have emptied the digits string append created string
            if len(digits) == 0:
                li.append(st)
            else:
                # for each character in the returned mapped value
                for char in m[digits[0]]:
                    # call this function again
                    # with initial string as the value from first char
                    # and potential new ones as the rest of digits string
                    check(st + char, digits[1:])

        if len(digits) == 0:
            return li
        else:
            check("", digits)
            return li
        
# SOLUTION AND EXPLANATION:
# this is the kind of problem i immediately knew recursion would be best for, as you can imagine this type of problem following a sort of solution tree.
# this specific problem calls for backtracking, as we need to generate all possible outcomes upon reaching each new digit

# uses O(3N * 4M) runtime and space, because we use a result array which stores all possible combinations. could be improved by using
# a more capable algorithm, like DFS
