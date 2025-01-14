# Given the root of a binary tree, invert the tree, and return its root.

#------------------------------------------------------------------------------------------


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # at each level we have to reverse the left and right 
        # if they exist

        if root is not None:
            if (root.left is not None and root.right is not None):
                tempNode = root.left
                tempNode2 = root.right
                root.left = tempNode2
                root.right = tempNode
                self.invertTree(root.left)
                self.invertTree(root.right)
            else:
                if root.left is not None:
                    self.invertTree(root.left)
                    root.right = root.left
                    root.left = None
                else:
                    self.invertTree(root.right)
                    root.left = root.right
                    root.right = None
        
        return root
            

# EXPLANATION AND COMPLEXITY:
# i knew that this problem would deal with some sort of recursion as we are dealing with binary trees
# what helped me to solve this problem was drawing out the problem and tracing the steps. i had the bulk of the code (at the top) but had to figure out how i would handle recursively calling on subtrees until
# i realized i should also call the invert tree before switching the side of a node with no sibling node

# uses O(n) complexity, does use a good bit of memory which means the algorithm could be improved. i havent looked into how, but i assume it would have to do with somehow making less checks 