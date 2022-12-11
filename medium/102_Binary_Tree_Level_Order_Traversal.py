# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS, O(n) runtime, O(n) memory (worse case O(n/2) for most nodes at a level)
        output = []
        
        q = collections.deque()
        q.append(root)

        while q:
            length = len(q)
            level = []
            for _ in range(length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                output.append(level)
            
        return output