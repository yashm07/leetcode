# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        
        # search for left node
        prev, curr = dummyNode, head
        for _ in range(left-1):
            prev = curr
            curr = curr.next
        
        left_node = curr
        prev_left = prev

        for _ in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        prev_left.next = prev    
        left_node.next = curr

        return dummyNode.next
        
        