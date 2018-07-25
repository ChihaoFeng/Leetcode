# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumber(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = node = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            node.next = ListNode(carry % 10)
            node = node.next
            carry //= 10
        return head.next

    def createListNode(self, nums):
        head = node = ListNode(-1)
        for num in nums:
            node.next = ListNode(num)
            node = node.next
        return head.next

    def printAsList(self, node):
        ret = []
        while node:
            ret.append(node.val)
            node = node.next
        return ret


"""
The idea is to iterate through two lists at the same time with the variable carry under the while loop.
The while loop will terminate only if both lists are empty and carry = 0.

Time: O(max(m+n))
Space: O(max(m+n)) the length of result is at most max(m+n) + 1
"""
L1 = Solution().createListNode([])
L2 = Solution().createListNode([9])
res = Solution().addTwoNumber(L1, L2)
print(Solution().printAsList(res))

L1 = Solution().createListNode([])
L2 = Solution().createListNode([])
res = Solution().addTwoNumber(L1, L2)
print(Solution().printAsList(res))

L1 = Solution().createListNode([5])
L2 = Solution().createListNode([5, 6])
res = Solution().addTwoNumber(L1, L2)
print(Solution().printAsList(res))

L1 = Solution().createListNode([2, 4, 3])
L2 = Solution().createListNode([5, 6, 4])
res = Solution().addTwoNumber(L1, L2)
print(Solution().printAsList(res))

L1 = Solution().createListNode([5, 3, 5])
L2 = Solution().createListNode([5, 6, 4])
res = Solution().addTwoNumber(L1, L2)
print(Solution().printAsList(res))
