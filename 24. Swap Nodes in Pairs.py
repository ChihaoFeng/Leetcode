# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = node = ListNode(-1)
        dummy.next = head
        while node.next and node.next.next:
            node1 = node.next
            node2 = node1.next
            node3 = node2.next
            node.next = node2
            node2.next = node1
            node1.next = node3
            node = node1
        return dummy.next

    def swapPairs_1(self, head):
        def swap_helper(node):
            if node and node.next:
                node1 = node.next
                node2 = node1.next
                node1.next = node
                node.next = swap_helper(node2)
                return node1
            return node
        return swap_helper(head)


"""
Sol1: iteration
Sol2: recursion

Time: O(n)
Space: O(1)
"""