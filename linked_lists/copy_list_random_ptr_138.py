# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. 
# Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. 

#-----------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        hm = {}
        curr = head

        # proceed through original list and create mappings
        # in hm which map old nodes to the created ones
        while curr:
            new_node = Node(x=curr.val)
            hm[curr] = new_node
            curr = curr.next
        
        # through curr again except now we add next and random ptrs
        # we can easily access the original pointers via hashmap
        curr = head
        while curr:
            new_node = hm[curr]
            if curr.next:
                new_node.next = hm[curr.next]
            else:
                new_node.next = None
            if curr.random:
                new_node.random = hm[curr.random]
            else:
                new_node.random = None

            curr = curr.next
        
        # at head key of hashmap we will have the entire list copied
        return hm[head]


# EXPLANATION AND COMPLEXITY:
# uses O(n) time complexity as we only need to process through the list once before we reconstruct it
# the hints state that we can/should use extra space to create a mapping of old to new nodes. then we can process through again
# to reconstruct the list by using the nodes and their pointers which are available in the hashmap for easy access