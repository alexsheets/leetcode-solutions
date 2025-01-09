# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#------------------------------------------------------------------------------------------------------------------------


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # want to recursively call something which adds 1 until 
        # we reach end of tree

        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

# EXPLANATION AND COMPLEXITY:
# this is a simple algorithm for understanding how binary trees and recursion can work hand in hand
# the function calls itself while adding 1 to add to the depth we have reached
# the function uses max() to check between the subtree of the left and right subtrees for their depth
# which should step all the way down the tree while calling itself and adding one