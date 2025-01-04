# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# Medium - Linked List

#----------------------------------------------------------------------------------------------------------


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        curr = head
        temp = head
        prev = None

        while curr:
            length += 1
            curr = curr.next 
        
        index = length - n

        if (index == 0):
            head = temp.next
            return head
        else:
            for i in range(1, index+1):
                prev = temp
                temp = temp.next
                if temp is None:
                    return head
            
            if temp is not None:
                prev.next = temp.next
                
        return head
    
# COMPLEXITY AND EXPLANATION:
# O(N) time complexity, has to check each element in list

# first, we loop through the linked list to get its length. then i subtract the position N from the length of the whole list. 
# using this position, we can loop through the linked list from start to our position, set the previous node as still in the linked list, and then see if the next element is none.
# if we reach the end/see that temp is none, we want to return the list 
# otherwise, after we have processed these positions in the list, and temp is not None, then we want to set our previous node's next pointer to the next pointer of our current element.


# once we have traversed the list using this method, it will return the linked list with the correct position from end of the list removed