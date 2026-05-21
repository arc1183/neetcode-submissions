# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        a=root
        while a:
            if val<a.val:
                if not a.left:
                    a.left=TreeNode(val)
                    break
                a=a.left
            elif val>a.val:
                if not a.right:
                    a.right=TreeNode(val)
                    break
                a=a.right
        return root