# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = node0 = ListNode(-1)
        large = node1 = ListNode(-1)
        while head:
            if head.val < x:
                node0.next = head
                node0 = node0.next
            else:
                node1.next = head
                node1 = node1.next
            head = head.next
        node0.next = large.next
        node1.next = None
        return small.next


"""
We use two dummy nodes: small and large. Then we traverse through the list,
if current list node's value is smaller than x, we append this node after small list. Otherwise, we
append this node after large list.


Time: O(n)
Space: O(n)
"""