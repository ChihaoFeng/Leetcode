# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        queue = collections.deque([root])
        level = []
        while queue and level:
            if not queue:
                ret.append([node.val for node in level])
                queue.extend(level)
                level.clear()
            node = queue.pop()
            if not node.left:
                level.append(node.left)
            if not node.right:
                level.append(node.right)