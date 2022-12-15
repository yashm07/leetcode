# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # O(n) runtime, 
        self.max_diameter = 0
    
        def dfs(root):
            if not root:
                return 0
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            self.max_diameter = max(self.max_diameter, left_height+right_height)
            return max(left_height, right_height)+1

        dfs(root)
        return self.max_diameter