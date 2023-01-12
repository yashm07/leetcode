# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNodeExtension(ListNode):
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force approach
        # # O(nlogn) time, O(n) space
        # nodes = []
        # for l in lists:
        #     while l:
        #         nodes.append(l.val)
        #         l = l.next
        
        # nodes.sort()
        # head = tail = ListNode(0)
        # for val in nodes:
        #     tail.next = ListNode(val, next=None)
        #     tail = tail.next
        
        # return head.next

        # another way of doing it is comparing k nodes at a time
        # most predictable way - using a min-heap and traverse through list and update final list in place
        # O(nlogk) time, O(k) space or O(n) if creating new linked list (easier to do)
        # interesting way to override method 
        ListNode.__lt__ = ListNodeExtension.__lt__
        min_heap = []
        
        for i, l in enumerate(lists):
            if l:
                heappush(min_heap, (l.val, l))
        
        # dummy node makes it easy to do in-place
        head = tail = ListNode(0)

        while min_heap:
            val, node = heappop(min_heap)
            tail.next = ListNode(val)
            tail = tail.next
            # move header of list
            if node.next:
                heappush(min_heap, (node.next.val, node.next))
        
        return head.next