# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 

#-----------------------------------------------------------------------------------------------------------------------


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return
        
        # use double ended queue for level order traversal
        q = deque()
        q.append(root)
        currLevel = 0

        result_arr = []
        final_arr = []

        while q:
            result_arr.append([])

            for i in range(len(q)):
                node = q.popleft()
                result_arr[currLevel].append(node.val)

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

            currLevel += 1
        
        for level in result_arr:
            val = 0
            nums = 0
            for data in level:
                nums += 1
                val += data
            final_arr.append(float(val / nums))
        
        return final_arr
    

# EXPLANATION AND COMPLEXITY:
# uses O(n) runtime as BFS uses O(n) complexity. the runtime of this algorithm is fast, but the memory usage was large. could be lessened by using recursion rather than iterative algorithm for BFS.
# the approach was simply to traverse the tree at each level, append an array for each level's nodes, and then average them afterward. the algorithm could also use less memory by finding a way to
# simply find average each time and append rather than calculating afterwards.