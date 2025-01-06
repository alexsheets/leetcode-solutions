# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#----------------------------------------------------------------------------------------------------------------------------------------


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for ch in s:
            if ch == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif ch == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif ch == "]":
                if not stack or stack.pop() != "[":
                    return False
            else:
                stack.append(ch)
            
        return not stack
    

# EXPLANATION AND COMPLEXITY:
# uses O(N) complexity as it only visits each element once
# the approach is simply to use a stack and loop through string, appending each opening bracket to it; when we close them, we pop it off of the stack
# at the end, if the stack is not empty, then that means it did not close all brackets