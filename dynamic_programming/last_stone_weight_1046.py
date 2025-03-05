# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

# At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone. If there are no stones left, return 0.

#----------------------------------------------------------------------------------------------------

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []

        for weight in stones:
            heapq.heappush(heap, weight)

        heapq.heapify(heap)

        while (len(heap) > 1):
            y = heapq.nlargest(2, heap)[0]
            x = heapq.nlargest(2, heap)[1]

            if (x == y):
                index = heap.index(x)
                heap[index] = heap[-1]
                heap.pop()
                index = heap.index(y)
                heap[index] = heap[-1]
                heap.pop()
            else:
                index = heap.index(x)
                heap[index] = heap[-1]
                heap.pop()
                index = heap.index(y)
                heap[index] = y-x
            
            heapq.heapify(heap)

        # heap now equal to 1 or 0
        if len(heap) == 0:
            return 0
        else:
            return heap[0]
        

# SOLUTION AND COMPLEXITY:
# this is a sort of brute force solution to this problem, to assist me in learning more about heap implementation in python.
# could be improved by using some python intricacies to create a max heap rather than normal one, which can simplify
# the operations necessary to perform to get the last stone weight.

# uses O(n log n) complexity, meaning the algorithm will scale logarithmically as the size of input grows.