"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # 3 ways to do this question
        # -> BFS using queue (O(n), O(n))
        # -> DFS using recursion (O(n), O(n))
        # -> BFS using two pointers (O(n), O(1))
        
        cur, nxt = root, root.left if root else None

        while nxt:
            cur.left.next = cur.right
            cur.right.next = cur.next.left if cur.next else None

            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        
        return root
