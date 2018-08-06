# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.prev and self.prev.val >= root.val:
                if not self.first:
                    self.first = self.prev
                self.second = root
            self.prev = root
            inorder(root.right)

        self.first = self.second = self.prev = None
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val


"""
e.g. inorder: 0 8 2 3 5 6 1
The idea is to find nodes with value 8 and 1, and switch the value between two nodes

Time: O(n)
Space: O(n)
"""
