# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ret.append(root.val)
            dfs(root.right)

        dfs(root)
        return min([ret[i] - ret[i - 1] for i in range(1, len(ret))])
