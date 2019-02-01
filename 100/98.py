# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ret = []

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            ret.append(root.val)
            in_order(root.right)

        in_order(root)
        leng = len(ret)
        for k in range(leng - 1):
            if ret[k] >= ret[k + 1]:
                return False
        return True
