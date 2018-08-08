# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(i, j):
            if i > j:
                return None
            m = (i + j) // 2
            root = TreeNode(nums[m])
            root.left = helper(i, m - 1)
            root.right = helper(m + 1, j)
            return root

        return helper(0, len(nums) - 1)