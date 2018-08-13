# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def preorder(root, count):
            if not root:
                return
            if not root.left and not root.right:
                count = count * 10 + root.val
                self.ret += count
                return
            count = count * 10 + root.val
            preorder(root.left, count)
            preorder(root.right, count)

        self.ret = 0
        preorder(root, 0)
        return self.ret