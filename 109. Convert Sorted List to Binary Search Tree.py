# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow = fast = head
        prev = None
        while fast.next and fast.next.next:
            prev, slow = slow, slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
            left = head
        else:
            left = None
        root = TreeNode(slow.val)
        right = slow.next
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
        return root
