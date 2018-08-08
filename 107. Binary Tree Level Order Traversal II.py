# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        queue = [root]
        ret = []
        while queue:
            ret.append([node.val for node in queue])
            queue = [child for node in queue for child in [node.left, node.right] if child]
        ret.reverse()
        return ret