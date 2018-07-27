# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse_helper(head):
            node0 = node1 = head
            for _ in range(k):
                if not node1:
                    return head
                node1 = node1.next
            prev = None
            while node0 != node1:
                temp = node0.next
                node0.next = prev
                prev = node0
                node0 = temp
            head.next = reverse_helper(node1)
            return prev

        return reverse_helper(head)

"""
Recursion

Time: O(n)
Space: O(1)
"""