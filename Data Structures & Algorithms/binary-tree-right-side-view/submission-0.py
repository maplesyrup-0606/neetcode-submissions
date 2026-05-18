# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        """
        bfs and get the last element to the results
        """
        if not root: return []

        level = deque([root])
        ret = []

        while level:
            n = len(level)
            for i in range(n):
                node = level.popleft()
                if i == n - 1:
                    ret.append(node.val)
                
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

        return ret