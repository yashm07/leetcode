from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find length of list
        if not head:
            return head
        last = head
        count = 1 
        while last.next != None:
            last = last.next
            count += 1
        
        # if k%count == 0:
        #     return head
        
        iter_count = count-k%count
        curr = head
        for _ in range(iter_count-1):
            curr = curr.next
        last.next = head
        head = curr.next
        curr.next = None

        return head

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head = sol.rotateRight(head, k=5)
while head != None:
    print(head.val)
    head = head.next
