# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dummy = node = RandomListNode(-1)
        memo = {None: None}
        while head:
            node.next = RandomListNode(head.label) if head not in memo else memo[head]
            node.next.random = RandomListNode(head.random.label) if head.random not in memo else memo[head.random]
            memo[head] = node.next
            node = node.next
            head = head.next
        return dummy.next
