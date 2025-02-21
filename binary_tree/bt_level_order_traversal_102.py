# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

#------------------------------------------------------------------------------------------------------

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.levelOrderRecursion(root, 0, result)
        return result
    
    def levelOrderRecursion(self, root, currLevel, result):
        if not root:
            return
        
        # add new level if necessary (we have more elements to process)
        if len(result) <= currLevel:
            result.append([])

        # add current node to current level we are at, continue for its children
        # will continue to recur until we have finished traversing
        result[currLevel].append(root.val)
        self.levelOrderRecursion(root.left, currLevel+1, result)
        self.levelOrderRecursion(root.right, currLevel+1, result)


# EXPLANATION AND COMPLEXITY: 
# this was a simple problem, as it is obvious we can use recursion to move down a binary tree. uses O(n) time and space complexity as we do not require 
# any extra checking or use of unnecessary structures to keep track of the result. 
# to progress down the binary tree, we simply call the recursive function from the original one, and allow the recursion to occur until done then return said result
# the recursive function should append a new array for each level and then add all elements at said level, and then do that for each level