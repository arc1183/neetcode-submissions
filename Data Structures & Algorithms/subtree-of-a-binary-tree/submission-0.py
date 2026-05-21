# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def findt(root,subroot):
            if not subroot:
                return True
            if not root:
                return False
            if equal(root,subroot):
                return True
            return (findt(root.left,subroot) or findt(root.right,subroot))                
        def equal(root,subroot):
            if not root and not subroot:
                return True
            if not root or not subroot or root.val != subroot.val:
                return False
            l=equal(root.left,subroot.left)
            r=equal(root.right,subroot.right)
            return l and r
        return findt(root,subRoot)