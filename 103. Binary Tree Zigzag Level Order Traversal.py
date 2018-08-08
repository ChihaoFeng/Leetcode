# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        ret = []
        flag = True
        while queue:
            if flag:
                ret.append([queue[i].val for i in range(len(queue))])
            else:
                ret.append([queue[i].val for i in range(len(queue) - 1, -1, -1)])
            queue = [node0 for node in queue for node0 in [node.left, node.right] if node0]
            flag = not flag
        return ret