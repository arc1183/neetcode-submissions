# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def diameter(root):
            nonlocal res
            if root is None:
                return 0
            
            a=diameter(root.left)
            b=diameter(root.right)
            res=max(res,a+b)
            return max(a,b)+1
        diameter(root)
        return res