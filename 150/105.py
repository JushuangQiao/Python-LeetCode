# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        loc = inorder.index(preorder[0])
        left, right = inorder[0:loc], inorder[loc+1:]
        root.left = self.buildTree(preorder[1:len(left)+1], left)
        root.right = self.buildTree(preorder[len(left)+1:] ,right)
        return root
