# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = []
        def dfs(r):
            if r.left: dfs(r.left)
            ret.append(r.val)
            if r.right: dfs(r.right)
        dfs(root)
        return min([abs(ret[i]-ret[i+1]) for i in range(len(ret)-1)])
