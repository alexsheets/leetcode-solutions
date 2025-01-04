# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#-----------------------------------------------------------------------------------------------------------

# by tracing the sequence of numbers, we can tell that this is a sort of fibonacci sequence
# where we can obtain the number of steps by adding the number of steps for two prior n's

class Solution:
    def climbStairs(self, n: int) -> int:
        finalNum = 0

        if (n == 1):
            return 1
        elif (n == 2):
            return 2
        elif (n == 3):
            return 3
        else:
            prevNum = 3
            prevNum2 = 2
            i = 4
            while i <= n:
                finalNum = prevNum + prevNum2
                if (i == n):
                    return finalNum
                else:
                    prevNum2 = prevNum
                    prevNum = finalNum
                    i= i+1


## COMPLEXITY: constant time, or O(N)
## keeps track of previous numbers so there is no need to look/perform extra checks

## SOLUTION EXPLANATION: simply iterates and adds the previous 2 step amounts until we reach n 
## at which point we return the number we have gotten to