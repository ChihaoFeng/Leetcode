# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postorder(root):
            if not root:
                return 0
            left = postorder(root.left)
            right = postorder(root.right)
            max_child = max(left, right)
            self.ret = max(self.ret, max_child + root.val, left + right + root.val, root.val)
            return root.val + max_child if max_child > 0 else root.val

        self.ret = float('-inf')
        postorder(root)
        return self.ret


"""
result can be left + right + root.val or max(left, right) + root.val or root.val
"""