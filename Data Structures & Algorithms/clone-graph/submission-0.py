"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {node.val: Node(node.val)}
        q = collections.deque([node])

        while q:
            curr = q.popleft()
            clone = visited[curr.val]
            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                clone.neighbors.append(visited[neighbor.val])

        return visited[node.val]