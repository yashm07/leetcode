# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) run time, O(n) space complexity due to call stack
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, num):
            if not root:
                return 0
            
            num = num * 10 + root.val
            if not root.right and not root.left:
                return num

            return dfs(root.left, num) + dfs(root.right, num)
        
        return dfs(root, 0)

