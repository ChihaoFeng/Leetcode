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
        while root:
            dummy = node = TreeLinkNode(-1)
            while root:
                if root.left:
                    node.next = root.left
                    node = node.next
                if root.right:
                    node.next = root.right
                    node = node.next
                root = root.next
            root = dummy.next
            del dummy
