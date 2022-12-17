# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # optimized approach - uses prefix sum: https://en.wikipedia.org/wiki/Prefix_sum
    # basically difference in two sums in prefix sum will tell you if target occurs in the path
    # O(n) runtime, O(n) space due to recursion call stack and storing prefix
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        sum_dict = {}
        cur_sum = 0

        def dfs(root, cur_sum):
            if not root:
                return

            cur_sum += root.val
            if cur_sum == targetSum:
                self.count += 1
            if (cur_sum - targetSum) in sum_dict:
                self.count += sum_dict[cur_sum-targetSum]
            
            if cur_sum in sum_dict:
                sum_dict[cur_sum] += 1 
            else:
                sum_dict[cur_sum] = 1
                
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)
            
            sum_dict[cur_sum] -= 1
        
        dfs(root, cur_sum)
        return self.count

    # brute force approach
    # bfs each node and solve path sum for each parent node using dfs
    # O(n^2) time complexity, O(n) memory due to stack/queue used in selecting the parent node
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    #     self.count = 0
    #     # stack = [root]
    #     queue = collections.deque()
    #     queue.append(root)

    #     while queue:
    #         top = queue.popleft()
    #         if top:
    #             queue.append(top.left)
    #             queue.append(top.right)

    #             self.dfs(top, targetSum)
        
    #     return self.count
    
    # def dfs(self, root, targetSum):
    #     if not root:
    #         return
        
    #     targetSum -= root.val
    #     if targetSum == 0:
    #         self.count += 1
        
    #     self.dfs(root.left, targetSum)
    #     self.dfs(root.right, targetSum)
        
        