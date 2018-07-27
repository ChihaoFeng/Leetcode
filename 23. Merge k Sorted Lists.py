class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge2Lists(l1, l2):
            head = node = ListNode(-1)
            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            node.next = l1 if l1 else l2
            return head.next

        def mergeKLists_helepr(i, j):
            if i == j:
                return lists[i]
            m = (i + j) // 2
            l1 = mergeKLists_helepr(i, m)
            l2 = mergeKLists_helepr(m + 1, j)
            return merge2Lists(l1, l2)

        if not lists:
            return None
        return mergeKLists_helepr(0, len(lists) - 1)


"""
The idea is to combine merge sort and merge two sorted lists

Time: O(Nlog(k)) k is the length of lists and N
Space: O(1)
"""