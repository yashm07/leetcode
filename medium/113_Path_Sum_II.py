# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.output = []
        self.__pathSum(root, targetSum, [])
        return self.output

    def __pathSum(self, root, targetSum, curPath):
        if not root:
            return
        curPath += [root.val]
        if not root.right and not root.left and root.val == targetSum:
            self.output.append(list(curPath))
        else:
            targetSum -= root.val
            self.__pathSum(root.left, targetSum, curPath)
            self.__pathSum(root.right, targetSum, curPath)
        
        curPath.pop()
