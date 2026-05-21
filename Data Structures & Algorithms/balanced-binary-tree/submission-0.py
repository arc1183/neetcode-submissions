# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res=True
        def balanced(root):
            if root is None:
                return 0
            a=balanced(root.left)
            b=balanced(root.right)
            if abs(a-b)>1:
                self.res=False
            return max(a,b)+1
        balanced(root)
        return self.res