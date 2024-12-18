# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

#-----------------------------------------------------------------------------------

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use BFS to traverse graph

        # instantiate two queues for the trees and start by appending first node
        queue1 = []
        queue2 = []

        queue1.append(p)
        queue2.append(q)

        # while the queues are not empty
        while (queue1 and queue2):

            # pop off first element for comparison
            curr1 = queue1.pop(0)
            curr2 = queue2.pop(0)

            # if they are both empty exit loop and return true
            if (curr1 == None and curr2 == None):
                continue
            
            # if one or the other is empty at any level and the other isnt, then they arent the same
            if (curr1 == None or curr2 == None):
                return False
            
            # also if the current vals we are looking at are not the same, trees are not same
            if (curr1.val != curr2.val):
                return False
            
            # after visiting first nodes, append the left and right values to the queues
            queue1.append(curr1.left)
            queue2.append(curr2.left)
            queue1.append(curr1.right)
            queue2.append(curr2.right)
        
        # if we have exited loop with no false conditions, the trees are the same
        return True
    

## COMPLEXITY: BFS uses O(V + E) complexity, where V is vertices and E is number of edges. This algorithm will explore in a breadth-first manner meaning the traversal 
# has a linear time complexity which is proportional to the sum of vertices and edges