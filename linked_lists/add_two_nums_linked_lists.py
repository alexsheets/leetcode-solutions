# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#-----------------------------------------------------------------

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = ''
        num2 = ''
        node = None
        
        while l1 is not None:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2 is not None:
            num2 = str(l2.val) + num2
            l2 = l2.next
        
        s = int(num1) + int(num2)
        sum_str = str(s)[::-1]

        node = ListNode(int(sum_str[0]))

        for i in range(1, len(sum_str)):
            new_node = ListNode(int(sum_str[i]))
            curr = node
            while curr.next:
                curr = curr.next
            
            curr.next = new_node


        return node


# COMPLEXITY AND EXPLANATION:
# return to rework for faster compilation
# but this initial solution does work