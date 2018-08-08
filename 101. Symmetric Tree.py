# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSymmetric_helper(root0, root1):
            if not root0 and not root1:
                return True
            if not root0 or not root1:
                return False
            if root0.val != root1.val:
                return False
            return isSymmetric_helper(root0.left, root1.right) and isSymmetric_helper(root0.right, root1.left)
        if not root:
            return True
        return isSymmetric_helper(root.left, root.right)


"""
Time: O(n)
Space: O(n)
"""