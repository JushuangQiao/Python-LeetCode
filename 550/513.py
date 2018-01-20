# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        d = deque()
        d.append(root)
        ret = root.val
        while d:
            node = d.popleft()
            ret = node.val
            if node.right:
                d.append(node.right)
            if node.left:
                d.append(node.left)
        return ret
