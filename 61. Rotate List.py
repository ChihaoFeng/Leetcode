# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        slow = fast = head
        length = 0
        _k = k
        while _k > 0:
            length += 1
            fast = fast.next
            if not fast:
                _k = k % length
                fast = head
            else:
                _k -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next if slow.next else head
        fast.next = head
        slow.next = None
        return new_head


"""
count the total length
Time: O(n)
Space: O(1)
"""