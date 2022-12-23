# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # O(n) runtime, O(n) memory due to call stack
        self.output = -inf

        def get_sum(node):
            if not node:
                return 0
            
            l_val, r_val = get_sum(node.left), get_sum(node.right)
            max_path = max(node.val + max(l_val, r_val), node.val)
            self.output = max(self.output, max_path, node.val+l_val+r_val)
            return max_path
        
        get_sum(root)
        return self.output
    