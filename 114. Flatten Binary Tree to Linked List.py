# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None
            right_head = dfs(root.right)
            left_head = dfs(root.left)
            root.left = None
            if left_head:
                root.right = left_head
                while left_head.right:
                    left_head = left_head.right
                left_head.right = right_head
            return root

        return dfs(root)