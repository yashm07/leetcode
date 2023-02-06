"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # dfs, O(n) or O(e+v) time, O(v) space
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_map = {}

        def dfs(node):
            if node in node_map:
                return node_map[node]

            if not node:
                return None

            copy = Node(node.val)
            node_map[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)

    # bfs, O(n) or O(e+v) time, O(v) space 
    # def cloneGraph(self, node: 'Node') -> 'Node':
    #     if not node: return None

    #     q = deque()
    #     visited = {}

    #     q.append(node)
    #     visited[node] = Node(node.val)

    #     while q:
    #         cur = q.popleft()
    #         cur_clone = visited[cur]

    #         for neighbor in cur.neighbors:
    #             if neighbor not in visited:
    #                 copy = Node(neighbor.val)
    #                 visited[neighbor] = copy
    #                 q.append(neighbor)
    #             cur_clone.neighbors.append(visited[neighbor])
        
    #     return visited[node]




        
        
