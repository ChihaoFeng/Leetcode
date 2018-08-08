class Solution:

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def postorder(root):
            if not root:
                return 0
            left = postorder(root.left)
            if left == -1:
                return -1
            right = postorder(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return postorder(root) != -1
