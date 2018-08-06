# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def allleft(root):
            while root:
                stack.append(root)
                root = root.left

        stack = []
        allleft(root)
        prev = float('-inf')
        while stack:
            node = stack.pop()
            if node.val <= prev:
                return False
            prev = node.val
            allleft(node.right)
        return True


"""
inorder iteration
Time: O(n) where n refers to number of nodes
Space: O(n)
"""
