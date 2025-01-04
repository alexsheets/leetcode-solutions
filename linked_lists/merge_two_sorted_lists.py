# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

#------------------------------------------------------------------------------------

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # handle base cases of lists being none
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1 is None and list2 is None:
            return None

        # compare head elements
        if (list1.val < list2.val):
            # if the list1 value is smaller, recursively call
            # function with next element of list1 and rest of list2
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # otherwise, move to next of list2 and merge with list1
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


# COMPLEXITY AND EXPLANATION:
# at first, i thought the problem solution would be much more complicated, and 
# tried to logically apply what i thought should happen in each case.
# then, after some errors, i realized that recursively calling the function to
# continue merging with the remainder of the list would be a much more simple answer.

# the solution works in O(N+M) complexity, N and M being the lengths of the lists, respectively
# as it would only need to make maximum checks of both lengths