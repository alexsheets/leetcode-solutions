# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.


#-------------------------------------------------------------------------------------------------------------------------


class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        # if child is leaf and the current node val equals left over sum then return true
        if not root.left and not root.right and root.val == targetSum:  
            return True
        # otherwise recursively call function and subtract the val of current node 
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    

# EXPLANATION AND COMPLEXITY:
# uses O(n) time and O(h) space. we use a depth first search to easily add each visited node until a leaf to a path sum
# recursively call that function to continue down left or right, whichever subtree exists
# once we have fully explored a branch and reached a leaf, the recursion unwinds back to previous node to explore another branch