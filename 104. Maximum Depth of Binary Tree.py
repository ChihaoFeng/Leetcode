# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0

        def dfs(depth, root):
            if not root:
                self.ret = max(self.ret, depth)
                return
            dfs(depth + 1, root.left)
            dfs(depth + 1, root.right)

        dfs(0, root)
        return self.ret