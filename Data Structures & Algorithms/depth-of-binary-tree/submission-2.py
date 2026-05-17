# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0


        length = 0
        level = deque([root])

        while level:
            n = len(level)

            for i in range(n):
                node = level.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                
            length += 1
        
        return length