class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m, n
        while i > 0 and j > 0:
            if nums1[i - 1] > nums2[j - 1]:
                nums1[i + j - 1] = nums1[i - 1]
                i -= 1
            else:
                nums1[i + j - 1] = nums2[j - 1]
                j -= 1
        if j > 0:
            nums1[:j] = nums2[:j]


"""
compare two nums from tail to head

Time: O(m+n)
Space: O(1)
"""