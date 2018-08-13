# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        queue = [root]
        while queue:
            temp = []
            for i in range(len(queue)):
                if i != len(queue) - 1:
                    queue[i].next = queue[i + 1]
                if queue[i].left:
                    temp.append(queue[i].left)
                if queue[i].right:
                    temp.append(queue[i].right)
            queue = temp