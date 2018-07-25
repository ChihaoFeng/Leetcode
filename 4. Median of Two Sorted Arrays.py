class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        p, r = 0, m
        while p <= r:
            q1 = (p + r) // 2  # number of elements on the left side if nums1
            q2 = (m + n + 1) // 2 - q1  # number of elements on the left side of nums2
            n1left = float('-inf') if q1 == 0 else nums1[q1 - 1]
            n1right = float('inf') if q1 == m else nums1[q1]
            n2left = float('-inf') if q2 == 0 else nums2[q2 - 1]
            n2right = float('inf') if q2 == n else nums2[q2]
            if n1left <= n2right and n2left <= n1right:
                return max(n1left, n2left) if (m + n) % 2 else (max(n1left, n2left) + min(n1right, n2right)) / 2
            elif n1left > n2right:
                r = q1 - 1
            else:
                p = q1 + 1
        raise ValueError


"""
0   1   2   3
| 2 |
| 1 | 2 | 3 |



q1 = (0 + 1) / 2 = 0                    0   1   2   3         index of boundary
                                =>      | 2              =>       ||
q2 = (1 + 3 + 1) / 2 - q1 = 2             1   2 | 3           index of the first right element on right side


if n1left <= n2right and n2left <= n1right, we have found the solution:
1. if the total length is odd, the solution will be the max of n1left and n2left
2. if the total length is even, the solution will be the average of the max of left side and min if right side

if n1left > n2right, it means the correct boundary is on the left side of nums1 => r = q1 - 1
otherwise, we need to move the correct boundary is on the right side of nums1 => p = q1 + 1     


Time: O(log(min(m,n)))
Space: O(1)
"""
