# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def preorder(root, path, count):
            if not root:
                return
            if not root.left and not root.right:
                if count + root.val == sum:
                    ret.append(path + [root.val])
                return
            path.append(root.val)
            count += root.val
            preorder(root.left, path, count)
            preorder(root.right, path, count)
            path.pop()
        ret = []
        preorder(root, [], 0)
        return ret