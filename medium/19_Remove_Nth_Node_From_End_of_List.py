# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers, O(n) time, O(1) space
        dummy_node = ListNode(0, head)
        prev = dummy_node

        ptr = head
        while ptr:
            if n > 0:
                n -= 1
            else:
                prev = prev.next
            ptr = ptr.next
        
        prev.next = prev.next.next

        return dummy_node.next
        