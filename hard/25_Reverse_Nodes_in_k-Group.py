# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # O(n) + O(n) = O(2n), O(n) run time, O(1) space complexity
        length = self.get_length(head)
        
        dummyNode = ListNode(0, head)
        prev, curr = dummyNode, head
        
        while length >= k:
            prev_left = prev
            left = curr

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            prev_left.next = prev
            left.next = curr
            prev = left

            length -= k
        
        return dummyNode.next
    
    def get_length(self, head) -> int:
        ptr = head
        length = 0
        while ptr != None:
            ptr = ptr.next
            length += 1
        return length



        
