class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        node = head
        tail = prev = None
        for _ in range(m - 1):
            tail, node = node, node.next
        subhead = node
        for _ in range(n - m + 1):
            temp = node.next
            node.next = prev
            prev, node = node, temp
        if tail:
            tail.next = prev
        subhead.next = node
        return head if tail else prev


"""
Time: O(n)
Space: O(n)
"""
