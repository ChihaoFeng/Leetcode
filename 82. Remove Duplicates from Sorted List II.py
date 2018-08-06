# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = node = prev = ListNode(None)
        dummy.next = head
        while head:
            if prev.val != head.val:
                if head.val != head.next.val:
                    node.next = head
                    node = node.next
            prev, head = head, head.next
        node.next = None
        return dummy.next


"""
The idea is to heave a prev pointing to the previous node
We first check whether the current node == prev node. If not equal,
we then check whether the next node == current node. if not equal, we can
move the node pointer one step next

Time: O(n)
Space: O(1)
"""
