# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

#---------------------------------------------------------------------------------------------------------------------


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # move inorder traversal from left and reverse traversal from right

        if root is None:
            return True

        # create two stacks for comparing left and right subtrees
        left_stack = []
        right_stack = []
        left_stack.append(root.left)
        right_stack.append(root.right)

        while left_stack and right_stack:
            # pop off curr pairof nodes
            node1 = left_stack.pop()
            node2 = right_stack.pop()

            # if both are null we can continue
            if node1 is None and node2 is None:
                continue

            # condition checking
            if node1 is None or node2 is None or node1.val != node2.val:
                return False

            # push subtrees in mirror order
            left_stack.append(node1.left)
            right_stack.append(node2.right)
            left_stack.append(node1.right)
            right_stack.append(node2.left)

        # if stacks are empty every element had a mirror pair and thus symmetric
        return len(left_stack) == 0 and len(right_stack) == 0
    

# EXPLANATION AND SOLUTION:
# this is a sort of brute force logic application to the solution, as the initial idea for me was to traverse from left and right while comparing the mirror elements
# uses O(N) complexity as each element only has to be visited once
# the stacks are appended to by appending opposite sided children in the same order so that they may be checked to see if they are symmetric