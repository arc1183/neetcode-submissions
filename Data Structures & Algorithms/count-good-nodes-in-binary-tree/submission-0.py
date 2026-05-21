# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        def good(root,x):
            if not root:
                return
            if root.val>=x:
                self.count+=1
                x=root.val
            good(root.left,x)
            good(root.right,x)
        good(root,root.val)
        return self.count