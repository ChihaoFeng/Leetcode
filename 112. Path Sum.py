# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def preorder(root, count):
            if not root:
                return False
            if not root.left and not root.right:
                if root.val + count == sum:
                    return True
            count += root.val
            if preorder(root.left, count):
                return True
            if preorder(root.right, count):
                return True
            return False

        return preorder(root, 0)