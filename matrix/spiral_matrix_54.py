# Given an m x n matrix, return all elements of the matrix in spiral order.

#------------------------------------------------------------------------------------------------


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # use moving boundaries while going top -> right -> down to bottom -> left -> up
        # after we process an outer piece/boundary, increment to shrink the matrix

        finalList = []
        topBound = 0
        leftBound = 0
        bottomBound = len(matrix)-1
        rightBound = len(matrix[0])-1

        # while we are within the valid boundaries of the matrix
        while leftBound <= rightBound and topBound <= bottomBound:

            # move right
            for i in range(leftBound, rightBound+1):
                finalList.append(matrix[topBound][i])
            topBound += 1

            # then down to bottom of arr
            for j in range(topBound, bottomBound+1):
                finalList.append(matrix[j][rightBound])
            rightBound -= 1

            if topBound <= bottomBound:
                # progress left using backwards stepping range
                for k in range(rightBound, leftBound-1, -1):
                    finalList.append(matrix[bottomBound][k])
                bottomBound -= 1
            
            if leftBound <= rightBound:
                # progress up using backwards stepping range 
                for m in range(bottomBound, topBound-1, -1):
                    finalList.append(matrix[m][leftBound])
                leftBound += 1



        return finalList
    

# EXPLANATION AND COMPLEXITY:
# uses O(M*N) complexity as in the worst case we have to visit each element of each array (which we do)
# the given hints for this problem said that we should use an algorithm which mimics exactly what the problem describes while using boundaries, 
# so it was clear that i needed boundaries that i could adjust while processing the matrix